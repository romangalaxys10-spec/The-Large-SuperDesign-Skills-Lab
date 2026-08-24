---
name: aquafix-hydro-ledger
description: AquaFix Hydro Ledger — Home services / emergency trade. Calm hydro-light trust system. Use when building interfaces that need this exact visual identity.
origin: vercel
source: https://aquafix-sandy.vercel.app
---

# AquaFix Hydro Ledger

> Light blue-white service system with deep navy ink, one rationed cyan accent and Syne display type. Built for emergency-trade businesses that must feel instant, licensed and calm at the same time.

- **Category:** Home services / emergency trade
- **Mood:** Calm hydro-light trust system
- **Source:** Live Vercel demo (built by Rommark.dev)
**Live reference:** [https://aquafix-sandy.vercel.app](https://aquafix-sandy.vercel.app)


## When to use this skill

Load this design system when the product is a **home services / emergency trade** and the brand voice is *calm hydro-light trust system*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #f6fafd;          /* page canvas */
  --surface: #ffffff;  /* cards, nav */
  /* ink */
  --ink: #081c2e;         /* headings */
  --ink-2: #314b60;      /* body */
  --muted: #5b7a93;     /* captions */
  --line: #dbe9f4;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #0891b2;
  --accent-soft: #d7f1f7;   /* tint backgrounds */
  --good: #059669;
  --hot: #ea580c;         /* urgency only */
  /* radii */
  --r-s: 10px; --r-m: 16px; --r-l: 24px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Syne', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
| Body / UI | `Instrument Sans', sans-serif` | Paragraphs, buttons, forms |

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
| ⚡ | **30-min arrival** | Live ETA routing to nearest crew |
| 📋 | **Tablet quote** | Fixed price approved before tools open |
| 🛡️ | **Leak-free warranty** | Pressure test + digital warranty card |
| 📍 | **Tbilisi & Batumi** | Two cities, one dispatch desk |
