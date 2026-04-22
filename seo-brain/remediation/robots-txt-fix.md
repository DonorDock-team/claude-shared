# robots.txt Fix — Step-by-Step

**Problem:** DonorDock's robots.txt currently blocks GPTBot, ClaudeBot, Google-Extended, CCBot, Applebot-Extended, Amazonbot, Bytespider, and meta-externalagent. Every competitor (DonorPerfect, Bloomerang, Network for Good, Givebutter, Neon One) blocks none. This is self-sabotage for the stated AEO/GEO strategy.

**Root cause:** Cloudflare's Managed Content Signal / Bot Management default policy. Not a conscious Webflow setting — inherited from Cloudflare's "protect my content from AI" default.

## Step 1: Log in to Cloudflare
- Go to https://dash.cloudflare.com
- Select zone: **donordock.com**

## Step 2: Find the AI bot blocking setting

Check these locations in order (setting location varies by Cloudflare plan):

### Option A: Security → Bots
- Navigate: Security (left sidebar) → Bots → Configure Super Bot Fight Mode
- Look for: "AI Scrapers and Crawlers" or "Content Signals"
- If set to "Block" → change to "Allow" or "Allow selectively"

### Option B: Security → Settings
- Navigate: Security → Settings
- Look for: "Block AI scrapers and crawlers" toggle
- If ON → turn OFF (or select "Content Signals" and allow specific bots)

### Option C: Rules → Managed Transforms
- Navigate: Rules → Managed Transforms
- Look for: a rule like "Block AI Bots" or "Add AI robots directives"
- If enabled → disable

### Option D: Rules → Transform Rules → Modify Response Header
- Navigate: Rules → Transform Rules
- Check if there's a rule modifying `/robots.txt` response
- If yes → review and edit

## Step 3: Verify the change

After toggling the setting:
- Wait 2-5 minutes for Cloudflare edge propagation
- Run: `curl -s https://www.donordock.com/robots.txt`
- Expected: the `User-agent: GPTBot` / `Disallow: /` lines should be GONE
- Only a minimal robots.txt should remain, like:
```
User-agent: *
Allow: /

Sitemap: https://www.donordock.com/sitemap.xml
```

## Step 4: Layer on Webflow robots.txt (redundant but explicit)

Even with Cloudflare fixed, add explicit AI bot allows in Webflow's robots.txt for maximum clarity:

1. Webflow Designer → Project Settings (top-right gear) → SEO tab
2. Find "robots.txt" section
3. Enter:
```
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: CCBot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: DuckAssistBot
Allow: /

User-agent: Mistral-AI-User
Allow: /

User-agent: cohere-ai
Allow: /

Sitemap: https://www.donordock.com/sitemap.xml
Sitemap: https://www.donordock.com/sitemap-index.xml
```
4. Save and publish site

## Step 5: Request re-crawl

- Google Search Console → Settings → Crawl stats → request re-crawl
- Bing Webmaster → Crawl Control → request re-crawl
- For AI engines: they'll pick up the change on their own crawl schedule (7-30 days)

## Strategic note

The decision to unblock AI crawlers is a brand/IP tradeoff:
- **Unblock:** DonorDock content becomes trainable/citable by AI. Citations in ChatGPT/Claude/Perplexity answers drive AEO traffic. Competitive pressure — every competitor allows AI crawl.
- **Keep blocked:** Protects content from training use. But also blocks AI citations. Competitors win the AI-Overview / ChatGPT-cited category by default.

For DonorDock's stated AEO strategy, **unblocking is required**. If there's a legal/brand-safety concern, discuss with leadership and legal first. The current block appears to be Cloudflare's default setting that was never consciously chosen.
