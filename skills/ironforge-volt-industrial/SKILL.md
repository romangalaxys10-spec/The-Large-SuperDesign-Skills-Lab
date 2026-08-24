---
name: ironforge-volt-industrial
description: IronForge Volt Industrial — Fitness / athletic club. Black industrial slab with acid-lime voltage. Use when building interfaces that need this exact visual identity.
origin: vercel
source: https://ironforge-bice.vercel.app
---

# IronForge Volt Industrial

> Archivo Black uppercase display on near-black panels with a single acid-lime (#E8FF47) voltage accent reserved for energy moments. Angled ticker band, stroked headline words, skewed stat bands.

- **Category:** Fitness / athletic club
- **Mood:** Black industrial slab with acid-lime voltage
- **Source:** Live Vercel demo (built by Rommark.dev)
**Live reference:** [https://ironforge-bice.vercel.app](https://ironforge-bice.vercel.app)


## When to use this skill

Load this design system when the product is a **fitness / athletic club** and the brand voice is *black industrial slab with acid-lime voltage*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #0a0a0b;          /* page canvas */
  --surface: #131316;  /* cards, nav */
  /* ink */
  --ink: #f4f4f2;         /* headings */
  --ink-2: #c7c7ca;      /* body */
  --muted: #9b9ba3;     /* captions */
  --line: rgba(255,255,255,.09);       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #e8ff47;
  --accent-soft: #1c2005;   /* tint backgrounds */
  --good: #4ade80;
  --hot: #ff5c33;         /* urgency only */
  /* radii */
  --r-s: 10px; --r-m: 18px; --r-l: 28px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Archivo Black', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
| Body / UI | `Space Grotesk', sans-serif` | Paragraphs, buttons, forms |

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
| 🏋️ | **Eleiko platform** | Competition-grade bars & plates |
| ❄️ | **Recovery zone** | 2°C plunge + 90°C sauna |
| 📊 | **InBody lab** | Scans feed your program |
| ⏰ | **24/7 access** | Members never wait |
