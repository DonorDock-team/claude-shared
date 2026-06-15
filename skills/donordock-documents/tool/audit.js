#!/usr/bin/env node
/*
 * audit.js — brand auditor for content blocks, templates, and generated PDFs.
 *
 * Scans .hbs / .css / .html files for:
 *   1. Hex / rgb / rgba colors NOT declared in tokens.css
 *   2. Fonts NOT in the approved set (Silka, Quicksand, system fallbacks)
 *   3. Emoji glyphs (which break the brand — Lucide SVGs / colored dots only)
 *
 * Exits 0 when only warnings exist, 1 when any errors are present. Errors are
 * emoji violations (hard rule); colors and fonts are warnings (correctable).
 *
 * Usage:
 *   node audit.js content-blocks                    # walk whole library
 *   node audit.js templates/sales-proposal/preview.html
 *   node audit.js content-blocks/cover-purple
 *   node audit.js --json content-blocks > audit.json
 */
import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { dirname, extname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const TOOL_DIR = __dirname;
const TOKENS_PATH = join(TOOL_DIR, "tokens.css");

/* ------------------------------------------------------------------------ */
/*  Approved fonts                                                          */
/* ------------------------------------------------------------------------ */
const APPROVED_FONTS = new Set(
  [
    "Silka",
    "Quicksand",
    "Inter",
    "Hanken Grotesk",
    "Dancing Script",
    "Dancingscript",
    "Arial",
    "system-ui",
    "sans-serif",
    "serif",
    "monospace",
    "ui-monospace",
    "ui-sans-serif",
    "ui-serif",
    "-apple-system",
    "BlinkMacSystemFont",
    "Segoe UI",
    "Cascadia Mono",
    "SFMono-Regular",
    "Menlo",
    "Brush Script MT",
    "cursive",
    "inherit",
    "initial",
    "unset",
  ].map((s) => s.toLowerCase())
);

/* ------------------------------------------------------------------------ */
/*  Emoji ranges                                                            */
/* ------------------------------------------------------------------------ */
// Common emoji Unicode ranges. ★ ✓ → arrows are explicitly allowed below.
const EMOJI_RANGES = [
  [0x1f300, 0x1f5ff], // Misc symbols & pictographs (🎁, 📊, etc.)
  [0x1f600, 0x1f64f], // Emoticons (😀)
  [0x1f680, 0x1f6ff], // Transport (🚀, 🚨)
  [0x1f700, 0x1f77f], // Alchemical
  [0x1f780, 0x1f7ff], // Geometric shapes ext (forbidden)
  [0x1f900, 0x1f9ff], // Supplemental symbols (🤖, 🦾)
  [0x1fa00, 0x1fa6f],
  [0x1fa70, 0x1faff],
];

// Glyphs in the above ranges (or symbol ranges) we EXPLICITLY allow.
// ★ ✓ ✦ → ↗ are intentional brand uses; · — – are typographic.
const ALLOWED_GLYPHS = new Set([
  "★",
  "✓",
  "✦",
  "→",
  "↗",
  "·",
  "—",
  "–",
  "…",
]);

/* ------------------------------------------------------------------------ */
/*  Token extraction                                                        */
/* ------------------------------------------------------------------------ */
function normalizeHex(hex) {
  let h = hex.toLowerCase().replace(/^#/, "");
  // Expand 3- and 4-char shorthand
  if (h.length === 3) h = h.split("").map((c) => c + c).join("");
  if (h.length === 4) h = h.split("").map((c) => c + c).join("");
  // Drop alpha if FF
  if (h.length === 8 && h.endsWith("ff")) h = h.slice(0, 6);
  return "#" + h;
}

function normalizeRgb(call) {
  // strip whitespace
  return call.replace(/\s/g, "").toLowerCase();
}

function extractAllowedColors() {
  const css = readFileSync(TOKENS_PATH, "utf8");
  const allowed = new Set();

  // Hex
  for (const m of css.matchAll(/#([0-9a-fA-F]{3,8})\b/g)) {
    allowed.add(normalizeHex(m[0]));
  }
  // rgb/rgba
  for (const m of css.matchAll(/rgba?\([^)]+\)/g)) {
    allowed.add(normalizeRgb(m[0]));
  }
  // hsl/hsla
  for (const m of css.matchAll(/hsla?\([^)]+\)/g)) {
    allowed.add(normalizeRgb(m[0]));
  }

  return allowed;
}

/* ------------------------------------------------------------------------ */
/*  Allowlist — values that are intentionally fluid (shadows, focus rings)  */
/* ------------------------------------------------------------------------ */
const ALLOWLIST_PATTERNS = [
  // Translucent overlays — used for borders, focus rings, glassmorphic effects
  /^rgba\(0,0,0,0\.0[2-9]\)$/,   // 0.02 - 0.09 black tints (subtle borders)
  /^rgba\(0,0,0,0\.1[0-9]?\)$/,  // 0.10 - 0.19 black tints (medium borders)
  /^rgba\(0,0,0,0\.2[0-9]?\)$/,
  /^rgba\(255,255,255,0\.[0-9]{1,3}\)$/, // any white overlay
  /^rgba\(15,23,42,0\.[0-9]{1,3}\)$/,    // slate-900 shadows
  /^rgba\(140,44,191,0\.[0-9]{1,3}\)$/,  // brand-purple overlays (focus, hover)
  /^rgba\(15,143,237,0\.[0-9]{1,3}\)$/,  // brand-blue overlays
];

function inAllowlist(value) {
  return ALLOWLIST_PATTERNS.some((re) => re.test(value));
}

/* ------------------------------------------------------------------------ */
/*  Findings                                                                */
/* ------------------------------------------------------------------------ */
function findColorViolations(content, allowed) {
  const findings = [];
  const lines = content.split("\n");

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Skip CSS comments to avoid flagging hex inside /* ... */
    if (/^\s*\*/.test(line) || /^\s*\/\//.test(line)) continue;

    // Skip lines that look like Handlebars or HTML comments
    if (/^\s*<!--/.test(line) || /^\s*\{\{!--/.test(line)) continue;

    // Hex
    for (const m of line.matchAll(/#([0-9a-fA-F]{3,8})\b/g)) {
      const normalized = normalizeHex(m[0]);
      if (!allowed.has(normalized)) {
        findings.push({
          type: "color",
          severity: "warn",
          line: i + 1,
          token: m[0],
          message: `Hex color ${m[0]} (normalized ${normalized}) is not in tokens.css`,
          context: line.trim().slice(0, 120),
        });
      }
    }

    // rgb / rgba
    for (const m of line.matchAll(/rgba?\([^)]+\)/g)) {
      const normalized = normalizeRgb(m[0]);
      if (!allowed.has(normalized) && !inAllowlist(normalized)) {
        findings.push({
          type: "color",
          severity: "warn",
          line: i + 1,
          token: m[0],
          message: `${m[0]} is not in tokens.css or allowlist`,
          context: line.trim().slice(0, 120),
        });
      }
    }

    // hsl / hsla
    for (const m of line.matchAll(/hsla?\([^)]+\)/g)) {
      const normalized = normalizeRgb(m[0]);
      if (!allowed.has(normalized) && !inAllowlist(normalized)) {
        findings.push({
          type: "color",
          severity: "warn",
          line: i + 1,
          token: m[0],
          message: `${m[0]} is not in tokens.css or allowlist`,
          context: line.trim().slice(0, 120),
        });
      }
    }
  }

  return findings;
}

function findFontViolations(content) {
  const findings = [];
  const lines = content.split("\n");

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const m = line.match(/font-family\s*:\s*([^;}]+)/i);
    if (!m) continue;

    const value = m[1].trim();
    if (value.toLowerCase().startsWith("var(")) continue;

    // Parse stack — handle quoted multi-word names
    const stack = value
      .split(",")
      .map((f) => f.trim().replace(/^['"]|['"]$/g, ""))
      .filter(Boolean);

    for (const font of stack) {
      if (!APPROVED_FONTS.has(font.toLowerCase())) {
        findings.push({
          type: "font",
          severity: "warn",
          line: i + 1,
          token: font,
          message: `Font "${font}" is not in the approved set (Silka, Quicksand, system fallbacks)`,
          context: line.trim().slice(0, 120),
        });
      }
    }
  }

  return findings;
}

function findEmojiViolations(content) {
  const findings = [];
  const lines = content.split("\n");

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    // codePointAt iteration to handle surrogate pairs
    let j = 0;
    while (j < line.length) {
      const cp = line.codePointAt(j);
      const ch = String.fromCodePoint(cp);

      if (!ALLOWED_GLYPHS.has(ch)) {
        for (const [lo, hi] of EMOJI_RANGES) {
          if (cp >= lo && cp <= hi) {
            findings.push({
              type: "emoji",
              severity: "error",
              line: i + 1,
              token: ch,
              message: `Emoji ${ch} (U+${cp.toString(16).toUpperCase()}) — use Lucide SVG icons or colored dots instead`,
              context: line.trim().slice(0, 120),
            });
            break;
          }
        }
      }

      j += ch.length;
    }
  }

  return findings;
}

function auditFile(filePath, allowedColors) {
  const content = readFileSync(filePath, "utf8");
  return [
    ...findColorViolations(content, allowedColors),
    ...findFontViolations(content),
    ...findEmojiViolations(content),
  ];
}

/* ------------------------------------------------------------------------ */
/*  Directory walking                                                       */
/* ------------------------------------------------------------------------ */
const AUDIT_EXTENSIONS = new Set([".hbs", ".css", ".html", ".htm"]);

function* walkFiles(root) {
  const stack = [root];
  while (stack.length > 0) {
    const cur = stack.pop();
    const stat = statSync(cur);
    if (stat.isDirectory()) {
      for (const entry of readdirSync(cur)) {
        if (entry === "node_modules" || entry.startsWith(".")) continue;
        stack.push(join(cur, entry));
      }
    } else if (stat.isFile()) {
      if (AUDIT_EXTENSIONS.has(extname(cur).toLowerCase())) yield cur;
    }
  }
}

/* ------------------------------------------------------------------------ */
/*  CLI                                                                     */
/* ------------------------------------------------------------------------ */
const args = process.argv.slice(2);
const jsonMode = args.includes("--json");
const positional = args.filter((a) => !a.startsWith("--"));

if (positional.length === 0) {
  console.error(
    "Usage: node audit.js [--json] <file-or-directory>\n" +
      "       node audit.js content-blocks\n" +
      "       node audit.js templates/sales-proposal/preview.html"
  );
  process.exit(1);
}

const target = positional[0];
if (!existsSync(target)) {
  console.error(`Path not found: ${target}`);
  process.exit(1);
}

const allowedColors = extractAllowedColors();

const allFindings = [];
let totalErrors = 0;
let totalWarnings = 0;

const targetStat = statSync(target);
const files = targetStat.isDirectory() ? Array.from(walkFiles(target)) : [target];

for (const file of files) {
  const findings = auditFile(file, allowedColors);
  if (findings.length === 0) continue;
  allFindings.push({ file, findings });
  for (const f of findings) {
    if (f.severity === "error") totalErrors++;
    else totalWarnings++;
  }
}

if (jsonMode) {
  console.log(
    JSON.stringify(
      {
        scanned: files.length,
        files_with_findings: allFindings.length,
        errors: totalErrors,
        warnings: totalWarnings,
        findings: allFindings.map((f) => ({
          file: relative(TOOL_DIR, f.file),
          findings: f.findings,
        })),
      },
      null,
      2
    )
  );
} else {
  if (allFindings.length === 0) {
    console.log(`✓ Brand audit passed — scanned ${files.length} files, no violations`);
  } else {
    for (const { file, findings } of allFindings) {
      console.log(`\n${relative(TOOL_DIR, file)}`);
      for (const f of findings) {
        const tag = f.severity === "error" ? "✗ ERROR" : "⚠ warn ";
        console.log(`  L${f.line.toString().padStart(4)} ${tag} ${f.type.padEnd(6)} ${f.message}`);
        console.log(`         | ${f.context}`);
      }
    }
    console.log(
      `\nSummary: ${totalErrors} error${totalErrors === 1 ? "" : "s"}, ` +
        `${totalWarnings} warning${totalWarnings === 1 ? "" : "s"} across ` +
        `${allFindings.length}/${files.length} files`
    );
  }
}

process.exit(totalErrors > 0 ? 1 : 0);
