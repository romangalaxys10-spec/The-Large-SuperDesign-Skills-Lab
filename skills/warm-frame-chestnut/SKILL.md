---
name: warm-frame-chestnut
description: Warm Frame Chestnut Portfolio — Personal portfolio / studio. White editorial with chestnut-framed device mockups and scrawled labels. Use when building interfaces that need this exact visual identity.
origin: superdesign
source: https://superdesign.dev/design-systems/warm-frame-portfolio-light
---

# Warm Frame Chestnut Portfolio

> Enhanced from superdesign.dev&#x27;s Warm Frame study: white-dominant editorial page built around chestnut-framed device mockups, hand-scrawled labels and a single black-underline link system.

- **Category:** Personal portfolio / studio
- **Mood:** White editorial with chestnut-framed device mockups and scrawled labels
- **Source:** superdesign.dev design-systems study (enhanced)

## When to use this skill

Load this design system when the product is a **personal portfolio / studio** and the brand voice is *white editorial with chestnut-framed device mockups and scrawled labels*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #fcfcfa;          /* page canvas */
  --surface: #ffffff;  /* cards, nav */
  /* ink */
  --ink: #24211c;         /* headings */
  --ink-2: #57534b;      /* body */
  --muted: #8b857b;     /* captions */
  --line: #e7e3da;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #8a5a33;
  --accent-soft: #f4efe7;   /* tint backgrounds */
  --good: #4a6741;
  --hot: #8a5a33;         /* urgency only */
  /* radii */
  --r-s: 6px; --r-m: 10px; --r-l: 16px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Fraunces', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
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
| 🖼️ | **Case studies** | Deep dives, not screenshots |
| ✍️ | **Process notes** | Sketches to shipped, annotated |
| 🎙️ | **Talks** | Config, Clarity, local meetups |
| 📬 | **Open for Q3** | One slot remaining |
