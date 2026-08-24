---
name: glowup-fraunces-atelier
description: GlowUp Fraunces Atelier — Beauty / wellness atelier. Warm cream editorial softness with rose italic voice. Use when building interfaces that need this exact visual identity.
origin: vercel
source: https://glowup-bice.vercel.app
---

# GlowUp Fraunces Atelier

> Cream-and-rose atelier system built on light-weight Fraunces serif display, centered composition, pill CTAs and floating glass chips. For appointment-only brands that whisper luxury.

- **Category:** Beauty / wellness atelier
- **Mood:** Warm cream editorial softness with rose italic voice
- **Source:** Live Vercel demo (built by Rommark.dev)
**Live reference:** [https://glowup-bice.vercel.app](https://glowup-bice.vercel.app)


## When to use this skill

Load this design system when the product is a **beauty / wellness atelier** and the brand voice is *warm cream editorial softness with rose italic voice*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #f7f1ea;          /* page canvas */
  --surface: #fffdf9;  /* cards, nav */
  /* ink */
  --ink: #2a211c;         /* headings */
  --ink-2: #60544b;      /* body */
  --muted: #96877b;     /* captions */
  --line: #e9ded1;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #b5674f;
  --accent-soft: #f3e0d8;   /* tint backgrounds */
  --good: #58806d;
  --hot: #c98d83;         /* urgency only */
  /* radii */
  --r-s: 8px; --r-m: 18px; --r-l: 30px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Fraunces', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
| Body / UI | `Nunito Sans', sans-serif` | Paragraphs, buttons, forms |

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
| ✂️ | **Signature balayage** | Hand-painted dimension & gloss finish |
| 🌿 | **Botanical lines** | Vegan, cruelty-free product bar only |
| 🕯️ | **Never double-booked** | One guest, full artist attention |
| 💌 | **After-care ritual** | Personal plan + 14-day check-in |
