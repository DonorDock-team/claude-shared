#!/usr/bin/env node
/*
 * preview.js — render a content block's template.hbs with its sample-data.json
 * and write a preview.html alongside it.
 *
 * Usage:
 *   node preview.js cover-purple
 *   node preview.js --all              # regenerate every block's preview
 *
 * Phase 2: produces preview.html. Phase 4 adds Puppeteer to emit preview.png.
 */
import { readFileSync, writeFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import Handlebars from "handlebars";

const __dirname = dirname(fileURLToPath(import.meta.url));
const TOOL_DIR = __dirname;
const BLOCKS_DIR = join(TOOL_DIR, "content-blocks");

function renderBlock(blockName) {
  const blockDir = join(BLOCKS_DIR, blockName);
  if (!existsSync(blockDir)) {
    throw new Error(`Content block not found: ${blockName}`);
  }
  const templatePath = join(blockDir, "template.hbs");
  const dataPath = join(blockDir, "sample-data.json");
  if (!existsSync(templatePath)) throw new Error(`Missing template.hbs in ${blockName}`);
  if (!existsSync(dataPath)) throw new Error(`Missing sample-data.json in ${blockName}`);

  const templateSrc = readFileSync(templatePath, "utf8");
  const data = JSON.parse(readFileSync(dataPath, "utf8"));
  const template = Handlebars.compile(templateSrc, { noEscape: false });
  const rendered = template(data);

  // Relative paths from the block's preview.html back to tokens/base/assets
  const tokensRel = relative(blockDir, join(TOOL_DIR, "tokens.css"));
  const baseRel = relative(blockDir, join(TOOL_DIR, "base.css"));

  const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>${blockName} — preview</title>
  <link rel="stylesheet" href="${tokensRel}" />
  <link rel="stylesheet" href="${baseRel}" />
  <style>
    /* Screen viewing chrome — not present in PDF output */
    body { background: #E5E7EB; padding: 2rem; }
    .preview-frame {
      max-width: 8.5in;
      margin: 0 auto;
      box-shadow: var(--shadow-lg);
      background: var(--bg-white);
    }
    .preview-label {
      max-width: 8.5in;
      margin: 0 auto 1rem;
      font-family: var(--font-primary);
      font-size: 0.75rem;
      color: #6B7280;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
  </style>
</head>
<body>
  <div class="preview-label">Content block · ${blockName} · rendered with sample-data.json</div>
  <div class="preview-frame">
    ${rendered}
  </div>
</body>
</html>
`;
  const outPath = join(blockDir, "preview.html");
  writeFileSync(outPath, html, "utf8");
  return outPath;
}

function listBlocks() {
  if (!existsSync(BLOCKS_DIR)) return [];
  return readdirSync(BLOCKS_DIR).filter((entry) => {
    const full = join(BLOCKS_DIR, entry);
    return statSync(full).isDirectory();
  });
}

const args = process.argv.slice(2);
if (args.length === 0) {
  console.error("Usage: node preview.js <block-name> | --all");
  process.exit(1);
}

const targets = args[0] === "--all" ? listBlocks() : [args[0]];
for (const block of targets) {
  try {
    const out = renderBlock(block);
    console.log(`✓ ${block} → ${relative(TOOL_DIR, out)}`);
  } catch (err) {
    console.error(`✗ ${block}: ${err.message}`);
    process.exitCode = 1;
  }
}
