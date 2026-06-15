---
name: weekly-deal-source-audit
description: Weekly audit of new business deal sources: AI classifies each deal via HDYHAU reasoning (no keyword code) and updates HubSpot. Reports results back.
---

You are running the weekly DonorDock new business deal source audit. Today's date is available via bash. Follow every step exactly.

---

## PHASE A - Pull this month's new business deals

Search HubSpot for deals where:
- pipeline = "default" (this is the Sales Pipeline's internal API value)
- dealtype = "newbusiness"
- createdate >= first day of current month
- createdate <= tomorrow (use tomorrow not today to avoid UTC midnight edge cases)

Fetch these properties for each deal: dealname, amount, dealstage, deal_source_main, deal_source, deal_source_drill_down_1, createdate, hs_analytics_source, hs_analytics_source_data_1, hs_analytics_source_data_2

Also fetch the associated contact for each deal and get their `how_did_you_hear_about_us_` property (note the trailing underscore - this is the exact HubSpot property name) plus their `hs_analytics_source`, `hs_analytics_source_data_1`, and `hs_analytics_source_data_2` for paid-vs-organic disambiguation.

---

## PHASE B - AI classify and update HubSpot

**Two-field model.** Every deal has both a top-level category (`deal_source_main`) and a specific drilldown (`deal_source`). Always write BOTH when reclassifying.

### `deal_source_main` (top-level) — allowed enum values
- Inbound - Organic
- Inbound - Paid
- Events
- Outbound
- Customer Referral
- Partner Referral
- Existing Customer
- BDR

### Source of truth priority
1. Contact's HDYHAU (`how_did_you_hear_about_us_`) — primary signal for category intent
2. Existing `deal_source_main` / `deal_source` value on the deal
3. HubSpot original traffic source (`hs_analytics_source`, `hs_analytics_source_data_1/2`) — last resort, BUT see the Paid Search rule below: paid attribution always overrides a vague "google" HDYHAU.

### Classification rules

- **Partner Referral** → `deal_source_main` = "Partner Referral". HDYHAU names a recognized DonorDock channel partner. Recognized partners and their `deal_source` enum values: OneCause, Avid, GoFundMe Pro (stored as "Classy" in HubSpot), Virtuous, Golden, We are for Good, Pledge It, Partner - Rooted Software, Referral - GHD, Community Boost / Community Boost - SDR / Community Boost - GAGA.
- IMPORTANT: If HDYHAU names a company or person that is NOT in this partner list, do NOT classify as Partner Referral — classify as Customer Referral instead.
- **Customer Referral (Word of Mouth)** → `deal_source_main` = "Customer Referral", `deal_source` = "Referral - Word of Mouth". HDYHAU indicates a personal referral, friend, colleague, or names a person/company not in the partner list.
- **Inbound - Organic (Organic Search)** → `deal_source_main` = "Inbound - Organic", `deal_source` = "SEO - Organic Search". HDYHAU indicates online search, Google, research, "found online", "looked it up", etc. **BUT first check `hs_analytics_source`** — if it's `PAID_SEARCH` (especially with `hs_analytics_source_data_1` containing "pmax", "google ads", "cpc", or an ad campaign name), classify as Inbound - Paid instead.
- **Inbound - Paid** → `deal_source_main` = "Inbound - Paid". User clicked a paid ad (Performance Max, Google Ads, paid social). Signals: `hs_analytics_source` = `PAID_SEARCH` or `PAID_SOCIAL`, or `hs_analytics_source_data_1` contains "pmax", "ad", "cpc", "campaign". HDYHAU saying just "google" is ambiguous — defer to the analytics source. For the `deal_source` drilldown: use "FACEBOOK" or "LINKEDIN" for paid social. For paid Google there is currently no Google Ads / Paid Search drilldown enum, so leave `deal_source` BLANK and flag it in the report. (If a Google Ads drilldown enum gets added, switch to that.)
- **Inbound - Organic (AI / ChatGPT)** → `deal_source_main` = "Inbound - Organic", `deal_source` = "AI". HDYHAU mentions ChatGPT, AI, Claude, Perplexity, or any AI assistant.
- **Events** → `deal_source_main` = "Events", `deal_source` = "Event". HDYHAU or context indicates a webinar, conference, or in-person event.
- **Existing Customer** → `deal_source_main` = "Existing Customer", `deal_source` = "Existing Customer". The deal is for an existing customer (upgrade, renewal, expansion, additional user).
- **Outbound / BDR** → `deal_source_main` = "Outbound" or "BDR", `deal_source` = "BDR Team" or "RB2B Lead". Deal came from outbound prospecting.
- **No Unknown deals**: Every deal must be classified. If HDYHAU is blank and no other signal exists, use best judgment based on deal name, rep, and analytics source.

### `deal_source` (drilldown) — full allowed enum
Email - Customer Drip, Email - Lead Drip, Email - Trial Drip, Referral - G2, FACEBOOK, LINKEDIN, WEB_CONTACT, WEB_CRM_LIVEDEMO, WEB_CRM_TRIAL, WEB_CRM_VIDEODEMO, WEB_RESOURCE_EBOOK, WEB_RESOURCE_EXCEL, Referral - Team - Matt, Referral - Team - Rob, Referral - Team - Sarah O'Brien, Referral - Word of Mouth, Referral - (use referral source field), Meeting - Excel Spreadsheet Expert, SEO - Organic Search, Website - Resources, OneCause, Classy, Event, Community Boost, Community Boost - SDR, Community Boost - GAGA, PLG, Calendly, Referral - GHD, Referral - Team - Pat, BDR Team, RB2B Lead, Virtuous, Golden, Existing Customer, Avid, We are for Good, Pledge It, Partner - Rooted Software, AI

**GoFundMe Pro note**: GoFundMe Pro is the current brand name for Classy. The HubSpot `deal_source` enum uses "Classy" as the internal value for this partner. Always write "Classy" to HubSpot when the source is GoFundMe Pro. Display "GoFundMe Pro" in any human-facing summary.

For each deal that needs updating, call `manage_crm_objects` to update `deal_source_main` AND `deal_source` (and optionally `deal_source_drill_down_1`) in HubSpot.

Track the count of deals reclassified this run (call this `reclassified_count`).

---

## PHASE C - Report results

Produce a concise summary in the final response:
- Total new business deals reviewed this month
- `reclassified_count` with a short table: deal name, HDYHAU signal, new `deal_source_main`, new `deal_source`, HubSpot link
- Any deals you left alone but flagged as ambiguous (e.g. HDYHAU conflicts with analytics source and you made a judgment call) so a human can sanity-check
- Any Inbound - Paid deals where the `deal_source` drilldown was left blank because no matching enum exists (e.g. Google Ads / PMax)
- No dashboard, no GitHub push, no Slack post — just the audit and the writebacks in HubSpot plus this report

Keep the report tight — tables or bullet lists, no lengthy prose.
