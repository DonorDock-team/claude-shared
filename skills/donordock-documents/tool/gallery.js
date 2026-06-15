#!/usr/bin/env node
/*
 * gallery.js — generates `gallery/index.html`, a visual library showing every
 * content block in the plugin side-by-side. Reads each block's meta.md for
 * its purpose summary and embeds the rendered preview.html in an iframe.
 *
 * Run after `node preview.js --all` to make sure all previews are fresh.
 *
 * Usage:
 *   node gallery.js
 */
import { readFileSync, writeFileSync, readdirSync, statSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const TOOL_DIR = __dirname;
const BLOCKS_DIR = join(TOOL_DIR, "content-blocks");
const GALLERY_DIR = join(TOOL_DIR, "gallery");

/* Per-block iframe heights. Add a row when a new block is created.
   Full-page blocks → 1100. Bands → 80. Cards/callouts → 400-700. */
const BLOCK_HEIGHTS = {
  "cover-purple": 1100,
  "header-band": 80,
  "footer-band": 80,
  "your-moment": 900,
  "tool-consolidation": 900,
  "platform-overview-quad": 900,
  "donor-intelligence-quad": 900,
  "onboarding-3phase": 700,
  "pricing-card-purple": 600,
  "why-donordock-stats": 900,
  "next-steps-numbered": 700,
  "quote-block": 200,
  "competitor-comparison-table": 280,
  "limited-time-offer-sidebar": 240,
  "feature-checklist-grid": 500,
  "before-after-chips": 280,
};

function listBlocks() {
  if (!existsSync(BLOCKS_DIR)) return [];
  return readdirSync(BLOCKS_DIR)
    .filter((entry) => {
      const full = join(BLOCKS_DIR, entry);
      return statSync(full).isDirectory();
    })
    .sort();
}

function extractPurpose(blockName) {
  const metaPath = join(BLOCKS_DIR, blockName, "meta.md");
  if (!existsSync(metaPath)) return "(no meta.md)";
  const md = readFileSync(metaPath, "utf8");
  /* Pull the first **Purpose:** line */
  const match = md.match(/\*\*Purpose:\*\*\s*(.+?)(?:\n|$)/);
  return match ? match[1].trim() : "(purpose not described in meta.md)";
}

function buildCard(blockName) {
  const purpose = extractPurpose(blockName);
  const height = BLOCK_HEIGHTS[blockName] ?? 600;
  const previewPath = `../content-blocks/${blockName}/preview.html`;
  return `
    <article class="block-card">
      <header class="block-card-head">
        <div class="block-card-name">${blockName}</div>
        <div class="block-card-purpose">${purpose}</div>
      </header>
      <div class="block-card-frame" style="height: ${height}px;">
        <iframe src="${previewPath}" loading="lazy" title="${blockName} preview"></iframe>
      </div>
    </article>
  `;
}

function build() {
  if (!existsSync(GALLERY_DIR)) mkdirSync(GALLERY_DIR, { recursive: true });
  const blocks = listBlocks();
  const cards = blocks.map(buildCard).join("\n");

  const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>DonorDock Document Templates — Content Block Library</title>
  <link rel="stylesheet" href="../tokens.css" />
  <link rel="stylesheet" href="../base.css" />
  <style>
    body {
      background: var(--bg-lightest-gray);
      padding: var(--space-xl) var(--space-lg);
      font-family: var(--font-primary);
      color: var(--text-primary);
    }
    .gallery-head {
      max-width: 1100px;
      margin: 0 auto var(--space-2xl);
    }
    .gallery-eyebrow {
      display: inline-flex;
      align-items: center;
      padding: 0.375rem 0.875rem;
      background: var(--brand-purple-light);
      color: var(--brand-purple);
      border-radius: var(--radius-pill);
      font-size: var(--type-label-size);
      font-weight: var(--type-label-weight);
      letter-spacing: var(--type-label-tracking);
      text-transform: uppercase;
    }
    .gallery-title {
      font-size: var(--type-h2-size);
      font-weight: var(--type-h2-weight);
      line-height: var(--type-h2-line);
      letter-spacing: var(--type-h2-tracking);
      margin-top: var(--space-md);
    }
    .gallery-subtitle {
      color: var(--text-secondary);
      max-width: 65ch;
      margin-top: var(--space-sm);
    }
    .gallery-stats {
      display: flex;
      gap: var(--space-lg);
      margin-top: var(--space-lg);
      padding-top: var(--space-md);
      border-top: 1px solid var(--border-light);
    }
    .gallery-stat-label {
      font-size: var(--type-overline-size);
      font-weight: var(--type-overline-weight);
      letter-spacing: var(--type-overline-tracking);
      text-transform: uppercase;
      color: var(--text-muted);
    }
    .gallery-stat-value {
      font-size: var(--type-h4-size);
      font-weight: var(--type-h4-weight);
      color: var(--text-primary);
    }
    .gallery-grid {
      max-width: 1100px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: var(--space-xl);
    }
    .block-card {
      background: var(--bg-white);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-md);
      overflow: hidden;
    }
    .block-card-head {
      padding: var(--space-md) var(--space-lg);
      border-bottom: 1px solid var(--border-light);
      display: flex;
      align-items: baseline;
      gap: var(--space-md);
    }
    .block-card-name {
      font-family: ui-monospace, SFMono-Regular, "Cascadia Mono", Menlo, monospace;
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--brand-purple);
      flex: 0 0 auto;
    }
    .block-card-purpose {
      color: var(--text-tertiary);
      font-size: var(--type-small-size);
    }
    .block-card-frame {
      width: 100%;
    }
    .block-card-frame iframe {
      width: 100%;
      height: 100%;
      border: 0;
      display: block;
    }
  </style>
</head>
<body>
  <header class="gallery-head">
    <span class="gallery-eyebrow">Content Block Library</span>
    <h1 class="gallery-title">${blocks.length} content blocks ready to compose.</h1>
    <p class="gallery-subtitle">
      Every block below is a pixel-locked Handlebars partial. Templates compose them into proposals,
      one-pagers, and other PDFs. Sales reps fill in copy; the layout never drifts.
    </p>
    <div class="gallery-stats">
      <div>
        <div class="gallery-stat-label">Blocks</div>
        <div class="gallery-stat-value">${blocks.length}</div>
      </div>
      <div>
        <div class="gallery-stat-label">Phase</div>
        <div class="gallery-stat-value">2 of 8</div>
      </div>
      <div>
        <div class="gallery-stat-label">Status</div>
        <div class="gallery-stat-value">In progress</div>
      </div>
    </div>
  </header>

  <main class="gallery-grid">
    ${cards}
  </main>
  <!-- generated by gallery.js · ${blocks.length} blocks · ${new Date().toISOString()} -->
</body>
</html>
`;
  const outPath = join(GALLERY_DIR, "index.html");
  writeFileSync(outPath, html, "utf8");
  console.log(`✓ Gallery written to ${relative(TOOL_DIR, outPath)} (${blocks.length} blocks)`);
}

build();
