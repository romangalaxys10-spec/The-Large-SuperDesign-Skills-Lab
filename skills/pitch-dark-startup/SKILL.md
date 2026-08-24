---
name: pitch-dark-startup
description: Pitch Dark Startup — Startup fundraising decks. Near-black investor deck with one electric accent and oversized proof numbers. Use when building slide decks / presentation HTML for this context.
origin: lab-slides
source: The Large SuperDesign Skills Lab
---

# Pitch Dark Startup

> Fundraising deck system: near-black canvas, single electric accent rationed to traction moments, 120px hero metrics, one message per slide, problem→solution→traction→ask arc.

- **Category:** Startup fundraising decks
- **Medium:** projected / shared-screen presentations (16:9), rendered here as scrollable HTML deck

## When to use this skill

Load when the deliverable is a **slide deck** — pitch, keynote, board review, training or analytics readout — and the voice is *near-black investor deck with one electric accent and oversized proof numbers*.

## Design tokens

```css
:root {
  --bg: #0b0d12; --surface: #141824;
  --ink: #f0f3fa; --muted: #8b93a7; --line: #232a3b;
  --accent: #6ee7b7; --accent-soft: #12241f;
  --good: #34d399; --hot: #fb7185;
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

Font pairing: `Space Grotesk` for display, `Inter` for support.

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
| `cover` | Company — one-line promise. | Logo + promise + round label. |
| `problem` | Enterprises waste 31% of cloud spend. | Problem quantified immediately. |
| `traction` | $84k MRR · 18% mo · churn 1.9% | Three numbers, nothing else. |
| `ask` | Raising $2M for 18 months runway. | Use of funds: 3 bars. |

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
