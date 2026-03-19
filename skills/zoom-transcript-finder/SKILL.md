---
name: zoom-transcript-finder
description: >
  Find and retrieve Zoom meeting transcripts, summaries, and recordings from any host
  on the account. Use this skill whenever someone asks to find a Zoom recording, pull a
  transcript, get a meeting summary, look up what was discussed in a call, or retrieve
  content from a past Zoom meeting or webinar. Also trigger when someone references a
  specific meeting by name, host, or date and wants the transcript, notes, or summary
  from it. Works for kick-off calls, demos, webinars, team meetings, or any recorded
  Zoom session. Even if the user doesn't say "Zoom" explicitly, trigger this skill when
  they ask about a recent call, meeting recording, or transcript that likely came from Zoom.
---

# Zoom Transcript & Summary Finder

Retrieve transcripts, AI summaries, and recording metadata from Zoom meetings and webinars.

## Available Zoom Tools

You have access to these Zoom tools via the Zapier MCP connector:

| Tool | What it does | Key input |
|------|-------------|----------|
| `zoom_find_meeting_webinar` | Search meetings by topic name or ID | `topic` (partial match) or `id` |
| `zoom_api_request_beta` | Raw Zoom API calls (most flexible) | `url`, `method` |
| `zoom_get_meeting_summary` | Get AI-generated meeting summary | `uuid` (URL-encoded) |
| `zoom_find_meeting_or_webinar_participants` | List who attended | `meeting_id` |

Note: `zoom_find_recording_and_download` exists but is unreliable. Use `zoom_api_request_beta` with the recordings endpoint instead (see "Retrieving Content" below).

## Finding a Meeting

The user will typically give you some combination of: a host name/email, a meeting title (or partial title), and/or an approximate date. Here's how to find the right meeting.

### Strategy 1: Search by topic (when you have a meeting name)

Use `zoom_find_meeting_webinar` with the `topic` parameter. This does a partial match, so "Kick Off" will find "Charlene Struebing Kick Off Call". Set `isExactMatch` to `"false"`.

```
zoom_find_meeting_webinar
  topic: "Kick Off"
  instructions: "Find meetings with this topic"
  output_hint: "meeting id, uuid, topic, start_time, host email, duration"
```

This is the fastest path when you know part of the meeting name. However, this tool can return stale or limited results for past meetings. If results look outdated or incomplete, switch to Strategy 2.

### Strategy 2: List meetings by host (when you have a host name/email)

Use `zoom_api_request_beta` to call the List Meetings API. This requires the host's email address.

```
zoom_api_request_beta
  method: "GET"
  url: "https://api.zoom.us/v2/users/{email}/meetings"
  querystring: "type=previous_meetings&page_size=30"
  instructions: "List recent meetings for this user"
  output_hint: "meeting id, uuid, topic, start_time, duration for each meeting"
```

If you don't have the exact email, ask the user rather than guessing. Zoom emails don't always follow obvious patterns (e.g., it might be `bbitzegaio@donordock.com` not `bridgette@donordock.com`).

### Strategy 3: Search by date range

Combine with Strategy 2 using `from` and `to` parameters:

```
zoom_api_request_beta
  method: "GET"
  url: "https://api.zoom.us/v2/users/{email}/meetings"
  querystring: "type=previous_meetings&from=2026-03-01&to=2026-03-19&page_size=30"
  instructions: "List meetings in this date range"
  output_hint: "meeting id, uuid, topic, start_time, duration"
```

### Strategy 4: Finding webinars specifically

Webinars use a different API endpoint than regular meetings. If the user mentions "webinar" or you can't find it in meetings, search webinars:

```
zoom_api_request_beta
  method: "GET"
  url: "https://api.zoom.us/v2/users/{email}/webinars"
  querystring: "type=past&page_size=30"
  instructions: "List past webinars for this user"
  output_hint: "webinar id, uuid, topic, start_time, duration for each webinar"
```

For webinar recordings, use the same recordings endpoint as meetings (it works for both).

### When you find multiple matches

Present the matches to the user with topic, date, and duration so they can confirm which one. Don't assume -- meetings with similar names happen regularly (e.g., weekly "Kick Off Call" for different clients).

## Retrieving Content

Once you have the right meeting, follow this fallback chain. Try each step in order and stop when you get usable content.

### Step 1: Try the AI Meeting Summary

The summary is Zoom's AI-generated recap with key topics, action items, and discussion points. It's concise and usually the most useful format.

```
zoom_get_meeting_summary
  uuid: "{meeting_uuid}"
  instructions: "Get the full meeting summary"
  output_hint: "complete summary text, key topics, action items, next steps"
```

**If it returns empty or fails**: Not all meetings have AI summaries generated. This happens especially with older meetings or if the host doesn't have the AI Companion feature enabled. Move to Step 2.

**If you get "Invalid meeting id"**: The UUID likely contains special characters. URL-encode it: `abc/123==` becomes `abc%2F123%3D%3D`. If it still fails, try double-encoding: `abc%252F123%253D%253D`.

### Step 2: Get recordings and look for a transcript file

```
zoom_api_request_beta
  method: "GET"
  url: "https://api.zoom.us/v2/meetings/{meeting_id}/recordings"
  instructions: "Get recording files for this meeting"
  output_hint: "recording file id, file_type, download_url, file_size, recording_type for each file"
```

Use the **numeric meeting ID** here (not the UUID) -- it's more reliable for this endpoint.

In the response, look for transcript files: `recording_type: "audio_transcript"` or `file_type: "TRANSCRIPT"`. If found, the `download_url` gives you the VTT transcript.

**If you get a scope error** (`cloud_recording:read:meeting_transcript`): The transcript file exists but the current API token can't download it. Let the user know a transcript exists but you can't access it due to permissions, and offer the recording metadata (duration, file sizes, participant count) as an alternative.

### Step 3: If no summary or transcript is available

Tell the user what you found (the meeting exists, here's the date/duration/participants) and what you couldn't retrieve (no AI summary generated, transcript not accessible). Offer to:
- Pull the participant list so they know who attended
- Check if there's a chat file in the recordings
- Suggest they check Zoom directly for the recording playback

## Common Pitfalls

These are real issues encountered in production:

1. **Meeting ID vs UUID**: The numeric meeting ID (e.g., `85678901234`) is different from the UUID (e.g., `abc123==`). The summary endpoint needs the UUID. The recordings endpoint works best with the meeting ID.

2. **Email guessing wastes time**: If the first email attempt returns "User does not exist", ask the user for the correct email immediately. Don't try multiple variations.

3. **UUID encoding**: UUIDs containing `/` or `//` must be URL-encoded when used in API paths. Try single encoding first, then double encoding if that fails.

4. **Empty summaries are normal**: Not every meeting has an AI summary. This isn't an error -- it means the feature wasn't enabled for that meeting. Fall back to the transcript file.

5. **Webinars vs meetings**: These are separate in Zoom's API. If you can't find a meeting by topic, check the webinars endpoint too.

## Output

Return the retrieved content (summary, transcript, or both) to the user. Present it clearly and let them decide what to do with it. If they want to take action (draft an email, write a recap, etc.), that's outside this skill's scope -- hand it off to whatever workflow or skill is appropriate.
