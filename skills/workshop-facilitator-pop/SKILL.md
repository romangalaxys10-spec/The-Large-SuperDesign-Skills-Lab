---
name: workshop-facilitator-pop
description: Workshop Facilitator Pop — Workshops / training / classrooms. High-contrast facilitation slides readable from the back row. Use when building slide decks / presentation HTML for this context.
origin: lab-slides
source: The Large SuperDesign Skills Lab
---

# Workshop Facilitator Pop

> Training-room system: minimum 32px body text, high-contrast ink-on-light with marker-yellow highlights, numbered activity slides, timer chips and instructions written as verbs.

- **Category:** Workshops / training / classrooms
- **Medium:** projected / shared-screen presentations (16:9), rendered here as scrollable HTML deck

## When to use this skill

Load when the deliverable is a **slide deck** — pitch, keynote, board review, training or analytics readout — and the voice is *high-contrast facilitation slides readable from the back row*.

## Design tokens

```css
:root {
  --bg: #fffef7; --surface: #ffffff;
  --ink: #101418; --muted: #5b6570; --line: #e2e4e0;
  --accent: #ffd60a; --accent-soft: #fff8d6;
  --good: #12805c; --hot: #e63946;
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

Font pairing: `Archivo` for display, `Inter` for support.

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
| `activity` | DISCUSS (5 min): pick your worst meeting. | Verb + time chip + bold instruction. |
| `highlight` | Marked with <mark>yellow</mark> only what matters | Highlighter rationing: ≤15 words/slide. |
| `timer` | ⏱ 04:59 | Full-slide timer state for exercises. |
| `recap` | 3 things you leave with | Numbered recap closes the session. |

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
