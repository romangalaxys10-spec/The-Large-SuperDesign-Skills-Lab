---
name: dataviz-standard-pro
description: DataViz Standard Pro — Analytics reviews / data-heavy reports. Colorblind-safe categorical palette with direct labeling discipline. Use when building slide decks / presentation HTML for this context.
origin: lab-slides
source: The Large SuperDesign Skills Lab
---

# DataViz Standard Pro

> Chart-first presentation system: Okabe-Ito colorblind-safe categorical palette, no gridline clutter, direct end-labels instead of legends, units in subtitles, one chart per slide.

- **Category:** Analytics reviews / data-heavy reports
- **Medium:** projected / shared-screen presentations (16:9), rendered here as scrollable HTML deck

## When to use this skill

Load when the deliverable is a **slide deck** — pitch, keynote, board review, training or analytics readout — and the voice is *colorblind-safe categorical palette with direct labeling discipline*.

## Design tokens

```css
:root {
  --bg: #fcfcfd; --surface: #ffffff;
  --ink: #1a1f2b; --muted: #667085; --line: #e4e7ec;
  --accent: #0072b2; --accent-soft: #e8f1fa;
  --good: #009e73; --hot: #d55e00;
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

Font pairing: `IBM Plex Sans` for display, `IBM Plex Sans` for support.

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
| `chart-title` | Revenue doubled while CAC held flat. | Insight titles, never 'Revenue chart'. |
| `direct-labels` | Lines labeled at line-end. | No legend boxes. Ever. |
| `units` | Subtitle carries units + period. | '€ millions, FY2024 vs FY2025' |
| `one-chart` | One exhibit per slide. | Two charts = two slides. |

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
