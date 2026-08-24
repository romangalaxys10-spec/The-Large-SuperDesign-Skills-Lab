---
name: sd-framer
description: Framer — Portfolio / editorial. Dark-mode system — enhanced from superdesign.dev study. Use when building interfaces that need this exact visual identity.
origin: superdesign
source: https://superdesign.dev/design-systems/framer
---

# Framer

> Framer design.md. Near-black IDE-like dark mode carrying a rationed electric-blue accent, rounded display sans headlines, and monospace/serif accent faces bo...

- **Category:** Portfolio / editorial
- **Mood:** Dark-mode system — enhanced from superdesign.dev study
- **Source:** superdesign.dev design-systems study (enhanced)

## When to use this skill

Load this design system when the product is a **portfolio / editorial** and the brand voice is *dark-mode system — enhanced from superdesign.dev study*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #0b0d12;          /* page canvas */
  --surface: #070f1d;  /* cards, nav */
  /* ink */
  --ink: #eef1f6;         /* headings */
  --ink-2: #bac1ce;      /* body */
  --muted: #8792a6;     /* captions */
  --line: #232a36;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #3b82f6;
  --accent-soft: #070f1d;   /* tint backgrounds */
  --good: #34d399;
  --hot: #326ed1;         /* urgency only */
  /* radii */
  --r-s: 8px; --r-m: 14px; --r-l: 20px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Inter Tight', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
| Body / UI | `Inter', sans-serif` | Paragraphs, buttons, forms |

Type scale (fluid): `clamp(2.6rem, 5.4vw, 4rem)` hero → `clamp(1.9rem, 3.4vw, 2.7rem)` h2 → `1rem` body → `.78–.85rem` labels/kickers with `letter-spacing:.16em` uppercase.

## Layout grammar

1. Sticky blurred nav (`backdrop-filter: blur(14px)`, border-bottom hairline)
2. Hero: kicker chip → oversized display headline → one-paragraph lede → max **two** CTAs → trust stats row
3. One accent gradient/glow maximum, confined to the hero region
4. Cards on `--surface` with `--line` hairlines; hover = translateY(-5px) + shadow lift
5. Rationed accent rule: accent appears in ≤10% of pixels (CTAs, active states, key numbers)
6. Section rhythm: `padding: 92px 0`; content max-width 1200px
7. Footer minimal: single line + credit link

## Signature components

| Element | Spec |
|---|---|
| Buttons | Pill or 8px radius; primary uses `--accent`, secondary is hairline outline |
| Kicker chip | Uppercase micro-label with dot/emoji + soft tint background |
| Feature card | Icon tile (24px radius) + title + muted copy + price/link footer |
| Stat band | Dashed-top row of number+label pairs |
| Testimonial | Stars → quote → avatar + name + context |
| Form fields | 1.5px borders, focus ring `0 0 0 4px --accent-soft` |

## Do / Don't

**Do**
- Keep gradients inside the hero only
- Use tabular numerals for prices/metrics
- Preserve generous whitespace (≥92px section gaps)

**Don't**
- Introduce a second accent hue
- Put accent color on large background areas (except designated media surface)
- Mix additional font families beyond the two defined here

## Demo files

- [`demo.html`](demo.html) — full landing demo in this system
- [`diagram.svg`](diagram.svg) — token anatomy diagram

## Reference features (content pattern)

| Icon | Feature | Copy |
|---|---|---|
| 🖼️ | **Selected work** | Case studies with process |
| ✍️ | **Writing** | Notes on craft |
| 🎙️ | **Talks** | Conference appearances |
| 📬 | **Contact** | Usually replies fast |
