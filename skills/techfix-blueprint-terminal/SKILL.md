---
name: techfix-blueprint-terminal
description: TechFix Blueprint Terminal — Electronics repair / technical lab. Blueprint-grid engineering terminal with teal instrumentation. Use when building interfaces that need this exact visual identity.
origin: vercel
source: https://techfix-five.vercel.app
---

# TechFix Blueprint Terminal

> IBM Plex Mono meets Space Grotesk on a blueprint grid canvas. Teal instrumentation accent, live station readouts, tracking timelines styled as shell output. For labs that prove precision.

- **Category:** Electronics repair / technical lab
- **Mood:** Blueprint-grid engineering terminal with teal instrumentation
- **Source:** Live Vercel demo (built by Rommark.dev)
**Live reference:** [https://techfix-five.vercel.app](https://techfix-five.vercel.app)


## When to use this skill

Load this design system when the product is a **electronics repair / technical lab** and the brand voice is *blueprint-grid engineering terminal with teal instrumentation*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #0a0e14;          /* page canvas */
  --surface: #10161f;  /* cards, nav */
  /* ink */
  --ink: #e3eaf4;         /* headings */
  --ink-2: #afbbcc;      /* body */
  --muted: #7c8ca5;     /* captions */
  --line: #1f2b3d;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #39e0d0;
  --accent-soft: #12262b;   /* tint backgrounds */
  --good: #4ade80;
  --hot: #fb6a5f;         /* urgency only */
  /* radii */
  --r-s: 10px; --r-m: 18px; --r-l: 26px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Space Grotesk', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
| Body / UI | `IBM Plex Mono', sans-serif` | Paragraphs, buttons, forms |

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
| 🔬 | **40x micro-soldering** | IC-level component repair |
| 🌡️ | **Thermal diagnostics** | FLIR fault hunting pre-teardown |
| 💾 | **Data resurrection** | NAND dumps from dead boards |
| 📦 | **Insured mail-in** | Nationwide courier both ways |
