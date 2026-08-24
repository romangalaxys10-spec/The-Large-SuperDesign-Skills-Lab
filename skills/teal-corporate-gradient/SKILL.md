---
name: teal-corporate-gradient
description: Teal Corporate Gradient Ledger — Enterprise B2B / corporate SaaS. Pale-gray canvas with full-width teal-to-cyan identity gradients. Use when building interfaces that need this exact visual identity.
origin: superdesign
source: https://superdesign.dev/design-systems/teal-ledger-corporate
---

# Teal Corporate Gradient Ledger

> Enhanced from superdesign.dev&#x27;s Teal Ledger Corporate: near-white pale-gray canvas, teal-to-cyan gradient identity used at full width, structured enterprise cards and sober data tables.

- **Category:** Enterprise B2B / corporate SaaS
- **Mood:** Pale-gray canvas with full-width teal-to-cyan identity gradients
- **Source:** superdesign.dev design-systems study (enhanced)

## When to use this skill

Load this design system when the product is a **enterprise b2b / corporate saas** and the brand voice is *pale-gray canvas with full-width teal-to-cyan identity gradients*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #fafbfc;          /* page canvas */
  --surface: #ffffff;  /* cards, nav */
  /* ink */
  --ink: #0f2027;         /* headings */
  --ink-2: #374a54;      /* body */
  --muted: #5f7482;     /* captions */
  --line: #e1e8ec;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #0d9488;
  --accent-soft: #e6f5f3;   /* tint backgrounds */
  --good: #0d9488;
  --hot: #ea580c;         /* urgency only */
  /* radii */
  --r-s: 10px; --r-m: 14px; --r-l: 18px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Manrope', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
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
| Buttons | Pill or 10px radius; primary uses `--accent`, secondary is hairline outline |
| Kicker chip | Uppercase micro-label with dot/emoji + soft tint background |
| Feature card | Icon tile (30px radius) + title + muted copy + price/link footer |
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
| 🔐 | **Row-level security** | Policies as code, tested |
| 📜 | **Audit trails** | Immutable, exportable logs |
| 🏢 | **SSO & SCIM** | Okta, Entra, Google out of box |
| 📉 | **99.99% SLA** | Multi-region failover |
