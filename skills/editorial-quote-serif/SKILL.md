---
name: editorial-quote-serif
description: Editorial Quote Serif — Keynotes / culture talks / memorials. Magazine pull-quote system: serif giants on warm paper. Use when building slide decks / presentation HTML for this context.
origin: lab-slides
source: The Large SuperDesign Skills Lab
---

# Editorial Quote Serif

> Presentation system built like a magazine feature: Fraunces serif at poster scale on warm cream, generous margins, thin gold rules, speaker name set small-caps beneath every quote.

- **Category:** Keynotes / culture talks / memorials
- **Medium:** projected / shared-screen presentations (16:9), rendered here as scrollable HTML deck

## When to use this skill

Load when the deliverable is a **slide deck** — pitch, keynote, board review, training or analytics readout — and the voice is *magazine pull-quote system: serif giants on warm paper*.

## Design tokens

```css
:root {
  --bg: #faf6ef; --surface: #fffdf8;
  --ink: #231f18; --muted: #93876f; --line: #e8dfcc;
  --accent: #b08d57; --accent-soft: #f3ead9;
  --good: #58806d; --hot: #b4552d;
}
```

## Projection typography

| Element | Size (at 1920×1080) | Rule |
|---|---|---|
| Cover title | 96–140px | May bleed margins |
| Statement / action titles | 44–64px | Full sentence allowed |
| Body / bullets | 32px minimum | **Never smaller** — back-row law |
| Captions / sources | 18–20px | Bottom-left corner |
| Hero metric | 120–200px | One per slide |

Font pairing: `Fraunces` for display, `Inter` for support.

## Slide grammar (deck assembly order)

1. Cover → promise, not agenda
2. Context / problem (quantified immediately)
3. Core content slides — ONE idea each
4. Section dividers between acts
5. Proof / traction / exhibits
6. Recap or Ask
7. Closer mirrors the cover

## Signature components

| Layout | Spec | Notes |
|---|---|---|
| `quote` | “Simplicity is the ultimate sophistication.” | 72–96px serif italic, hanging quote mark. |
| `attribution` | — LEONARDO DA VINCI | Small caps, letter-spaced, muted gold. |
| `chapter` | II. The Craft | Roman numeral section divider. |
| `closer` | Thank you — questions welcome. | Same scale as cover, mirrored margin. |

## Do / Don't

**Do**
- Test readability: squint from 3 meters — if unreadable, font goes bigger
- One message per slide; split instead of shrinking
- Put sources and dates on-slide, bottom-left

**Don't**
- Bullet walls (max 4 lines × 6 words)
- Decorative stock photos that repeat the title
- Animations other than simple appear/fade

## Demo files

- [`demo.html`](demo.html) — the deck rendered in-browser
- [`diagram.svg`](diagram.svg) — layout anatomy: cover/content/chart/quote patterns
