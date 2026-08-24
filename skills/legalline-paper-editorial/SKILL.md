---
name: legalline-paper-editorial
description: LegalLine Paper Editorial — Legal / professional services. Cream-paper law journal with gold double rules. Use when building interfaces that need this exact visual identity.
origin: vercel
source: https://legalline.vercel.app
---

# LegalLine Paper Editorial

> Anthropic-inspired editorial system: Cormorant Garamond headlines with italic gold accents, Sora body, numbered practice cards and a dark estimator panel. Authority without coldness.

- **Category:** Legal / professional services
- **Mood:** Cream-paper law journal with gold double rules
- **Source:** Live Vercel demo (built by Rommark.dev)
**Live reference:** [https://legalline.vercel.app](https://legalline.vercel.app)


## When to use this skill

Load this design system when the product is a **legal / professional services** and the brand voice is *cream-paper law journal with gold double rules*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #faf7f2;          /* page canvas */
  --surface: #ffffff;  /* cards, nav */
  /* ink */
  --ink: #211d18;         /* headings */
  --ink-2: #554d42;      /* body */
  --muted: #8a7d6c;     /* captions */
  --line: #e8e1d5;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #9a6b15;
  --accent-soft: #f3e8d2;   /* tint backgrounds */
  --good: #2e7d5b;
  --hot: #ca8a04;         /* urgency only */
  /* radii */
  --r-s: 6px; --r-m: 12px; --r-l: 20px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Cormorant Garamond', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
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
| Buttons | Pill or 6px radius; primary uses `--accent`, secondary is hairline outline |
| Kicker chip | Uppercase micro-label with dot/emoji + soft tint background |
| Feature card | Icon tile (18px radius) + title + muted copy + price/link footer |
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
| 🏛️ | **IC structuring** | 1% regime built audit-ready |
| ⚖️ | **Arbitration** | GIAC & courts, partner-led |
| 🔍 | **M&A diligence** | Red-flag report inside a week |
| ™️ | **IP enforcement** | Sakpatenti & EUIPO filings |
