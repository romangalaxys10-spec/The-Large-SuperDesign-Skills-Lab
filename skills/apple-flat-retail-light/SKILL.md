---
name: apple-flat-retail-light
description: Apple Flat Retail Light — Consumer hardware retail. Flat off-white panels with edge-to-edge product renders. Use when building interfaces that need this exact visual identity.
origin: superdesign
source: https://superdesign.dev/design-systems/apple
---

# Apple Flat Retail Light

> Enhanced from superdesign.dev&#x27;s Apple study: flat off-white panel sections, edge-to-edge product imagery, SF-style system stack and a single rationed blue lifted only for links.

- **Category:** Consumer hardware retail
- **Mood:** Flat off-white panels with edge-to-edge product renders
- **Source:** superdesign.dev design-systems study (enhanced)

## When to use this skill

Load this design system when the product is a **consumer hardware retail** and the brand voice is *flat off-white panels with edge-to-edge product renders*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #f5f5f7;          /* page canvas */
  --surface: #ffffff;  /* cards, nav */
  /* ink */
  --ink: #1d1d1f;         /* headings */
  --ink-2: #454549;      /* body */
  --muted: #6e6e73;     /* captions */
  --line: #d2d2d7;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #0071e3;
  --accent-soft: #e8e8ed;   /* tint backgrounds */
  --good: #1d1d1f;
  --hot: #0071e3;         /* urgency only */
  /* radii */
  --r-s: 8px; --r-m: 12px; --r-l: 18px;
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
| 💻 | **M-series chips** | Fastest in every laptop class |
| 📷 | **Pro cameras** | Compute photography on-device |
| 🔒 | **Privacy built-in** | On-device processing default |
| ♻️ | **Recycled aluminum** | Carbon neutral by 2030 |
