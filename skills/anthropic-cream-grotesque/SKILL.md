---
name: anthropic-cream-grotesque
description: Anthropic Cream Grotesque Editorial — AI research / long-form product. Cream-paper editorial pairing bold grotesque with serif voice. Use when building interfaces that need this exact visual identity.
origin: superdesign
source: https://superdesign.dev/design-systems/anthropic
---

# Anthropic Cream Grotesque Editorial

> Enhanced from superdesign.dev&#x27;s Anthropic study: cream paper background, ink-black bold grotesque display paired with a serif for long-form voice, rationed single accent and generous margins.

- **Category:** AI research / long-form product
- **Mood:** Cream-paper editorial pairing bold grotesque with serif voice
- **Source:** superdesign.dev design-systems study (enhanced)

## When to use this skill

Load this design system when the product is a **ai research / long-form product** and the brand voice is *cream-paper editorial pairing bold grotesque with serif voice*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #f0eee6;          /* page canvas */
  --surface: #faf9f5;  /* cards, nav */
  /* ink */
  --ink: #181614;         /* headings */
  --ink-2: #43403b;      /* body */
  --muted: #6e6a63;     /* captions */
  --line: #dedbd2;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #c96442;
  --accent-soft: #e8e3d9;   /* tint backgrounds */
  --good: #527a5e;
  --hot: #c96442;         /* urgency only */
  /* radii */
  --r-s: 4px; --r-m: 8px; --r-l: 14px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Styrene-like', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
| Body / UI | `Lora', sans-serif` | Paragraphs, buttons, forms |

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
| Buttons | Pill or 4px radius; primary uses `--accent`, secondary is hairline outline |
| Kicker chip | Uppercase micro-label with dot/emoji + soft tint background |
| Feature card | Icon tile (12px radius) + title + muted copy + price/link footer |
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
| 📚 | **Research index** | 50+ peer-reviewed papers |
| 🛡️ | **Safety first** | Interpretability as a discipline |
| 🤝 | **Responsible scaling** | Published capability thresholds |
| 🛠️ | **API products** | Claude models for builders |
