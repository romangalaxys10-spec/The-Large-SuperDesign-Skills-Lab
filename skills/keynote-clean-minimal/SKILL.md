---
name: keynote-clean-minimal
description: Keynote Clean Minimal — Product launches / keynotes. Apple-style minimalism: one idea per slide, giant type. Use when building slide decks / presentation HTML for this context.
origin: lab-slides
source: The Large SuperDesign Skills Lab
---

# Keynote Clean Minimal

> Slide system distilled from Apple keynote language: white or black canvas, one idea per slide, display type so large it becomes the graphic, zero decoration.

- **Category:** Product launches / keynotes
- **Medium:** projected / shared-screen presentations (16:9), rendered here as scrollable HTML deck

## When to use this skill

Load when the deliverable is a **slide deck** — pitch, keynote, board review, training or analytics readout — and the voice is *apple-style minimalism: one idea per slide, giant type*.

## Design tokens

```css
:root {
  --bg: #000000; --surface: #111114;
  --ink: #f5f5f7; --muted: #86868b; --line: #2d2d30;
  --accent: #2997ff; --accent-soft: #1c1c1e;
  --good: #30d158; --hot: #f56300;
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

Font pairing: `Inter Tight` for display, `Inter` for support.

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
| `cover` | One word. Huge. | The entire keynote on one slide. |
| `statement` | Design is how it works. | No bullet points. No logos. Just the sentence. |
| `product` | [ Product render fills 90% ] | Caption optional. 48px max. |
| `number` | 2× faster | Single metric, 200px numerals. |

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
