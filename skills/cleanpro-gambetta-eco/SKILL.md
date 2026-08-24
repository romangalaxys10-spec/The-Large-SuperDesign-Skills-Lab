---
name: cleanpro-gambetta-eco
description: CleanPro Gambetta Eco-Minimal — Cleaning / facility services. White eco-minimalism with emerald italic serif. Use when building interfaces that need this exact visual identity.
origin: vercel
source: https://cleanpro-snowy-sigma.vercel.app
---

# CleanPro Gambetta Eco-Minimal

> Near-white minimal canvas, Gambetta serif italics as the only flourish, one emerald accent, dashed-line stat bands and a mint quote panel. Whitespace does the selling.

- **Category:** Cleaning / facility services
- **Mood:** White eco-minimalism with emerald italic serif
- **Source:** Live Vercel demo (built by Rommark.dev)
**Live reference:** [https://cleanpro-snowy-sigma.vercel.app](https://cleanpro-snowy-sigma.vercel.app)


## When to use this skill

Load this design system when the product is a **cleaning / facility services** and the brand voice is *white eco-minimalism with emerald italic serif*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #fbfdfc;          /* page canvas */
  --surface: #ffffff;  /* cards, nav */
  /* ink */
  --ink: #122a22;         /* headings */
  --ink-2: #475f55;      /* body */
  --muted: #7d9488;     /* captions */
  --line: #dfece5;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #0f9d6c;
  --accent-soft: #e4f6ee;   /* tint backgrounds */
  --good: #0f9d6c;
  --hot: #0a6e4b;         /* urgency only */
  /* radii */
  --r-s: 12px; --r-m: 20px; --r-l: 32px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Gambetta', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
| Body / UI | `Sora', sans-serif` | Paragraphs, buttons, forms |

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
| 🧼 | **Post-renovation** | HEPA extraction room by room |
| 📸 | **Photo log proof** | Checklist after every visit |
| 🌱 | **100% eco chemistry** | Plant-based, ESG certificates |
| 🔁 | **24h re-clean** | Guaranteed, no questions |
