---
name: mckinsey-consult-deck
description: McKinsey Consult Deck — Consulting / board presentations. Governing-thought titles over evidence: pyramid principle on slides. Use when building slide decks / presentation HTML for this context.
origin: lab-slides
source: The Large SuperDesign Skills Lab
---

# McKinsey Consult Deck

> Consulting-grade system: every slide title is a full-sentence action title stating the takeaway, body is one exhibit (chart/table) plus a source line, horizontal logic flows left-to-right.

- **Category:** Consulting / board presentations
- **Medium:** projected / shared-screen presentations (16:9), rendered here as scrollable HTML deck

## When to use this skill

Load when the deliverable is a **slide deck** — pitch, keynote, board review, training or analytics readout — and the voice is *governing-thought titles over evidence: pyramid principle on slides*.

## Design tokens

```css
:root {
  --bg: #ffffff; --surface: #f4f6f8;
  --ink: #051c2c; --muted: #5c6870; --line: #d4d9de;
  --accent: #2251ff; --accent-soft: #eef2fc;
  --good: #00806a; --hot: #c0392b;
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

Font pairing: `Georgia` for display, `Inter` for support.

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
| `action-title` | Churn costs €4.2M annually, concentrated in month-3 cohorts. | Action title = full sentence takeaway. |
| `exhibit` | [ Waterfall chart: revenue bridge ] | Unit economics in axis labels. Source bottom-left, 10pt. |
| `so-what` | So what: fix onboarding week 2–3 first. | Kicker 'So what' + recommendation box. |
| `next-steps` | Owner, deadline, metric — one row each. | Next-steps table closes every deck. |

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
