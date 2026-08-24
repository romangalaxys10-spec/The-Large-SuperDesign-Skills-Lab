---
name: autopro-voltage-dark
description: AutoPro Voltage Dark — Automotive / performance workshop. Near-black engineering garage with rationed red voltage. Use when building interfaces that need this exact visual identity.
origin: vercel
source: https://autopro-pi.vercel.app
---

# AutoPro Voltage Dark

> Carbon-black workshop system with uppercase Chakra Petch display type, hairline grid overlays and a single red accent reserved for CTAs and live telemetry.

- **Category:** Automotive / performance workshop
- **Mood:** Near-black engineering garage with rationed red voltage
- **Source:** Live Vercel demo (built by Rommark.dev)
**Live reference:** [https://autopro-pi.vercel.app](https://autopro-pi.vercel.app)


## When to use this skill

Load this design system when the product is a **automotive / performance workshop** and the brand voice is *near-black engineering garage with rationed red voltage*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #08090d;          /* page canvas */
  --surface: #0f1117;  /* cards, nav */
  /* ink */
  --ink: #eceef2;         /* headings */
  --ink-2: #bbc0cc;      /* body */
  --muted: #8b93a7;     /* captions */
  --line: #232634;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #ff3b2f;
  --accent-soft: #1a1013;   /* tint backgrounds */
  --good: #34d399;
  --hot: #ffb020;         /* urgency only */
  /* radii */
  --r-s: 8px; --r-m: 14px; --r-l: 20px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Chakra Petch', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
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
| 🖥️ | **OBD-II factory scan** | Full ECU health across all modules |
| ⚡ | **Dyno remapping** | Stage 1–2 validated on the roller |
| ⚙️ | **DSG / ZF service** | Mechatronics, fluids, adaptations |
| 🏁 | **Track alignment** | Laser camber & corner balance |
