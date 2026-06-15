#!/usr/bin/env node
/*
 * build.js — assemble a complete document from a template definition.
 *
 * A template definition (templates/<name>/definition.json) describes a
 * "spine" — an ordered list of pages, each of which is either a single
 * content block or a composition of several stacked content blocks.
 *
 * A data file (typically templates/<name>/sample-data.json) supplies:
 *   - document_meta : prepared_for, doc_label, dates, etc. — used by chrome
 *   - options       : map of block-name → boolean toggles for optional pages
 *                     and block-name → string choices for variant slots
 *   - blocks        : map of block-name → the data payload that block expects
 *
 * The script resolves the spine into a sequence of rendered pages, wraps each
 * interior page with header-band + footer-band, and writes a single HTML file.
 *
 * Usage:
 *   node build.js <template-name> [data.json] [output.html]
 *   node build.js sales-proposal
 *   node build.js sales-proposal ../../Deliverables/Proposals/Acme.json
 *
 * Defaults: if data file or output file aren't given, falls back to
 *   templates/<name>/sample-data.json and templates/<name>/preview.html.
 */
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import Handlebars from "handlebars";

const __dirname = dirname(fileURLToPath(import.meta.url));
const TOOL_DIR = __dirname;
const BLOCKS_DIR = join(TOOL_DIR, "content-blocks");
const TEMPLATES_DIR = join(TOOL_DIR, "templates");

const CHROME_HEADER_BLOCK = "header-band";
const CHROME_FOOTER_BLOCK = "footer-band";

/* ------------------------------------------------------------------------ */
/*  Block compilation                                                       */
/* ------------------------------------------------------------------------ */
const blockCache = new Map();

function compileBlock(blockName, data) {
  if (!blockCache.has(blockName)) {
    const path = join(BLOCKS_DIR, blockName, "template.hbs");
    if (!existsSync(path)) {
      throw new Error(`Content block not found: ${blockName}`);
    }
    const src = readFileSync(path, "utf8");
    blockCache.set(blockName, Handlebars.compile(src, { noEscape: false }));
  }
  return blockCache.get(blockName)(data || {});
}

/* ------------------------------------------------------------------------ */
/*  Spine resolution                                                        */
/* ------------------------------------------------------------------------ */

/**
 * Decide whether an optional step (page or composed block) should render.
 * - If `options[name]` is defined, that value wins (true/false override).
 * - Otherwise, fall back to step.default (defaults to true if undefined).
 */
function isStepEnabled(step, options, name) {
  if (!step.optional) return true;
  const key = name || step.content_block;
  if (options && Object.prototype.hasOwnProperty.call(options, key)) {
    return Boolean(options[key]);
  }
  return step.default !== false;
}

/* ------------------------------------------------------------------------ */
/*  Page rendering                                                          */
/* ------------------------------------------------------------------------ */
function renderPage(pageSpec, data) {
  const options = data.options || {};
  const blocksData = data.blocks || {};

  // Collect the content blocks to render on this page
  let composeList;
  if (Array.isArray(pageSpec.compose)) {
    composeList = pageSpec.compose;
  } else if (pageSpec.content_block) {
    composeList = [{ content_block: pageSpec.content_block }];
  } else {
    throw new Error(`Page spec missing content_block or compose: ${JSON.stringify(pageSpec)}`);
  }

  const renderedBlocks = composeList
    .filter((b) => isStepEnabled(b, options, b.content_block))
    .map((b) => compileBlock(b.content_block, blocksData[b.content_block]))
    .join("\n");

  if (pageSpec.no_chrome) {
    return renderedBlocks;
  }

  const headerHTML = compileBlock(CHROME_HEADER_BLOCK, {
    prepared_for: data.document_meta?.header_label || data.document_meta?.prepared_for || "",
  });
  const footerHTML = compileBlock(CHROME_FOOTER_BLOCK, {
    doc_label: data.document_meta?.doc_label || "DonorDock · donordock.com",
    right_label: data.document_meta?.right_label,
  });

  return `<section class="page">
${headerHTML}
${renderedBlocks}
${footerHTML}
</section>`;
}

/* ------------------------------------------------------------------------ */
/*  Template build                                                          */
/* ------------------------------------------------------------------------ */
function loadTemplate(templateName) {
  // Look in canonical templates/ first, then team-added templates/_team/
  const candidates = [
    join(TEMPLATES_DIR, templateName),
    join(TEMPLATES_DIR, "_team", templateName),
  ];
  for (const dir of candidates) {
    const defPath = join(dir, "definition.json");
    if (existsSync(defPath)) {
      const def = JSON.parse(readFileSync(defPath, "utf8"));
      return { def, dir };
    }
  }
  throw new Error(
    `Template not found: ${templateName}. Looked in ${candidates
      .map((c) => relative(TOOL_DIR, c))
      .join(" and ")}`
  );
}

function buildTemplate(templateName, data, outPath) {
  const { def } = loadTemplate(templateName);
  const options = data.options || {};

  const pageHTMLs = def.spine
    .filter((step) => isStepEnabled(step, options, step.content_block))
    .map((step) => renderPage(step, data));

  // Compute relative path from the output file's directory back to TOOL_DIR.
  // This handles outputs in templates/<name>/, templates/_team/<name>/, or
  // any user-supplied path (e.g., ~/Documents/.../Deliverables/Proposals/X.html).
  const cssRelDir = relative(dirname(outPath), TOOL_DIR) || ".";

  return wrapInHTMLShell({
    title:
      data.document_meta?.title ||
      `${data.document_meta?.prepared_for || templateName} — ${templateName}`,
    body: pageHTMLs.join("\n"),
    cssRelDir,
  });
}

function wrapInHTMLShell({ title, body, cssRelDir }) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>${escapeHtml(title)}</title>
  <link rel="stylesheet" href="${cssRelDir}/tokens.css" />
  <link rel="stylesheet" href="${cssRelDir}/base.css" />
  <style>
    /* Screen viewing chrome — not present in PDF output. Each .page renders
       on a contained "sheet" with a soft shadow against the gray screen bg. */
    body { background: #E5E7EB; padding: 0; }
    .page,
    .page-cover {
      max-width: 8.5in;
      min-height: 11in;
      margin: 2rem auto;
      box-shadow: var(--shadow-lg);
      background: var(--bg-white);
    }
    .page-cover { padding: var(--space-4xl) var(--space-3xl); }
    .page       { padding: 0.6in 0.55in; }
  </style>
</head>
<body>
${body}
<!-- built by build.js · ${new Date().toISOString()} -->
</body>
</html>
`;
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

/* ------------------------------------------------------------------------ */
/*  CLI                                                                     */
/* ------------------------------------------------------------------------ */
const args = process.argv.slice(2);
const flags = new Set(args.filter((a) => a.startsWith("--")));
const positional = args.filter((a) => !a.startsWith("--"));

if (positional.length === 0) {
  console.error(
    "Usage: node build.js [--no-audit] <template-name> [data.json] [output.html]"
  );
  process.exit(1);
}

const templateName = positional[0];
// Resolve the template dir up front so default data/output paths land beside it
const { dir: templateDir } = loadTemplate(templateName);
const dataPath = positional[1]
  ? resolve(positional[1])
  : join(templateDir, "sample-data.json");
const outPath = positional[2]
  ? resolve(positional[2])
  : join(templateDir, "preview.html");

const data = JSON.parse(readFileSync(dataPath, "utf8"));
const html = buildTemplate(templateName, data, outPath);
writeFileSync(outPath, html, "utf8");
console.log(`✓ ${templateName} → ${relative(TOOL_DIR, outPath)}`);

/* ------------------------------------------------------------------------ */
/*  Post-build hook: run brand auditor on the generated output              */
/* ------------------------------------------------------------------------ */
if (!flags.has("--no-audit")) {
  const auditScript = join(TOOL_DIR, "audit.js");
  if (existsSync(auditScript)) {
    console.log(""); // blank line for readability
    const result = spawnSync("node", [auditScript, outPath], {
      stdio: "inherit",
      cwd: TOOL_DIR,
    });
    if (result.status !== 0) {
      console.error(
        "\n✗ Brand audit found errors. Build output was still written, but it has hard-rule violations (e.g., emoji icons). Fix before sharing."
      );
      process.exit(result.status);
    }
  }
}
