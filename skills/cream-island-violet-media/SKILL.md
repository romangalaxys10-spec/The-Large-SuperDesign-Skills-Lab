---
name: cream-island-violet-media
description: Cream Island Violet Media — Creative agency / portfolio. Cream-and-charcoal around one saturated violet media surface. Use when building interfaces that need this exact visual identity.
origin: superdesign
source: https://superdesign.dev/design-systems/cream-island
---

# Cream Island Violet Media

> Enhanced from superdesign.dev&#x27;s Cream Island study: cream-and-charcoal base built around one saturated violet media surface, coral highlight rationing and oversized display type.

- **Category:** Creative agency / portfolio
- **Mood:** Cream-and-charcoal around one saturated violet media surface
- **Source:** superdesign.dev design-systems study (enhanced)

## When to use this skill

Load this design system when the product is a **creative agency / portfolio** and the brand voice is *cream-and-charcoal around one saturated violet media surface*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #efece6;          /* page canvas */
  --surface: #f7f5f0;  /* cards, nav */
  /* ink */
  --ink: #22201d;         /* headings */
  --ink-2: #4d4a44;      /* body */
  --muted: #79746b;     /* captions */
  --line: #ddd8cf;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #5b3df5;
  --accent-soft: #e6e1f7;   /* tint backgrounds */
  --good: #2f7d54;
  --hot: #ff7a59;         /* urgency only */
  /* radii */
  --r-s: 14px; --r-m: 22px; --r-l: 32px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Clash Display', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
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
| Buttons | Pill or 14px radius; primary uses `--accent`, secondary is hairline outline |
| Kicker chip | Uppercase micro-label with dot/emoji + soft tint background |
| Feature card | Icon tile (42px radius) + title + muted copy + price/link footer |
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
| 🎬 | **Film & motion** | Campaign films end-to-end |
| 🎨 | **Identity systems** | Logos that survive decades |
| 🕹️ | **Interactive** | WebGL experiences that ship |
| 🏆 | **Award bait** | Cannes Lions, D&AD, FWA |
