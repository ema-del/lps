# Pacow GHL Funnel — Working Rules

This repo holds the HTML/CSS/JS sections for Pacow's GHL (GoHighLevel) landing
page funnel. It is not a buildable app — each file in `ghl-sections/` is a
self-contained block pasted directly into a GHL custom-code element.

## Source of truth

- `ghl-sections/*.html` is the source of truth for the live GHL page, in
  paste order (`section-1-hero.html`, `section-2-...`, etc. — see
  `ghl-sections/README.md`).
- Whenever the page changes, the file changes first. GHL itself is never
  the source of truth — it's just where the file gets pasted.

## Workflow for every edit request

1. **Edit the actual file(s)** in `ghl-sections/`, not a scratch copy.
2. **Commit and push** to the working branch after every change (small or
   large) — don't batch unrelated changes into one commit.
3. **Reply with a find-and-replace patch, not the whole section**, unless
   the whole section is what's needed (e.g. pasting into a brand-new GHL
   page). For each change:
   - name the file
   - say where it lives (CSS in `<style>` vs. HTML markup vs. `<script>`)
   - show the **exact old text to find** and the **exact new text to
     replace it with**, as separate copy-pastable blocks
   - if the same text appears more than once, say which occurrence(s)
4. **Always end with a link to the full file** on GitHub (swap the
   filename in the URL) in case a full re-paste is easier than patching:
   `https://github.com/ema-del/lps/blob/<branch>/ghl-sections/<file>`
5. Never invent a GitHub PR unless explicitly asked for one.

## GHL constraints (why sections look the way they do)

- No `<head>`, `<html>`, or `<body>` tags — GHL strips them.
- No external stylesheets or build tools — Google Fonts only via `@import`
  inside a `<style>` tag.
- All images/media use absolute URLs (GHL doesn't serve local files).
- CSS classes are BEM-style and prefixed per section (`.pacow-hero__x`,
  `.pacow-how__x`, etc.) so they never collide with GHL's own CSS or with
  each other.
- Section 1 defines `window.pacowModal()` — every later section's CTA
  button calls `onclick="pacowModal('open')"`. Section 1 must always be
  pasted first in GHL.
- Every section must work if pasted alone — no cross-section CSS/JS
  dependencies except the `pacowModal` call above.

## Brand + copy rules

- Keep Pacow's visual system: void-black grid background with purple
  (`#7C3AFF`) accents on dark sections, white/off-white cards with a faint
  grid on light sections, Inter font, the existing button/badge/pill
  patterns. Don't introduce a new visual language without being asked.
- When adapting copy from a reference/competitor page (e.g. "make it more
  like X's page"): match the **structure and tone**, not their specific
  business facts — swap their niche/claims for Pacow's real ones (e.g.
  "coaching business" → "education business", their numbers → Pacow's
  actual numbers). Never invent a deliverable, stat, or claim that isn't
  already established elsewhere on the page.
- If the same fact appears in more than one section (a cadence, a number,
  a claim), keep it consistent everywhere when it changes — e.g. changing
  "weekly" to "bi-weekly" in one section means checking every other
  section that repeats it.
- Don't add specific counts/numbers (like "15-20 ads") unless asked for —
  prefer general phrasing when the client doesn't want to commit to a
  number publicly.

## When scope is ambiguous

Ask before doing a large rewrite (e.g. "restyle to match X" could mean a
light copy pass or a full page restructure) — a couple of quick multiple
choice questions up front beats redoing a big edit.
