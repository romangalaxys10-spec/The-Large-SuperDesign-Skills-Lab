---
name: wise-ultra-black-lime
description: Wise Ultra-Black Lime — Fintech / money transfer. Lime-saturated hero with ultra-black condensed display. Use when building interfaces that need this exact visual identity.
origin: superdesign
source: https://superdesign.dev/design-systems/wise
---

# Wise Ultra-Black Lime

> Enhanced from superdesign.dev&#x27;s Wise study: light-mode-dominant pages led by a lime-saturated hero block, ultra-black condensed display face, hairline utility buttons and big honest numbers.

- **Category:** Fintech / money transfer
- **Mood:** Lime-saturated hero with ultra-black condensed display
- **Source:** superdesign.dev design-systems study (enhanced)

## When to use this skill

Load this design system when the product is a **fintech / money transfer** and the brand voice is *lime-saturated hero with ultra-black condensed display*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #ffffff;          /* page canvas */
  --surface: #f2f7f2;  /* cards, nav */
  /* ink */
  --ink: #163300;         /* headings */
  --ink-2: #2d3d22;      /* body */
  --muted: #454745;     /* captions */
  --line: #e4ebe4;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #9fe870;
  --accent-soft: #eaf7dd;   /* tint backgrounds */
  --good: #2f5711;
  --hot: #ff4f00;         /* urgency only */
  /* radii */
  --r-s: 12px; --r-m: 16px; --r-l: 24px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Archivo Black', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
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
| Buttons | Pill or 12px radius; primary uses `--accent`, secondary is hairline outline |
| Kicker chip | Uppercase micro-label with dot/emoji + soft tint background |
| Feature card | Icon tile (36px radius) + title + muted copy + price/link footer |
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
| 💱 | **Mid-market rate** | The real rate, always shown |
| 💸 | **Tiny fees** | Up to 6x cheaper than banks |
| 🌍 | **160 countries** | Send to 80+ currencies |
| 🏦 | **FSC protected** | Safeguarded customer funds |
