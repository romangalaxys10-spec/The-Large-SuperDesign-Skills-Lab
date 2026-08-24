---
name: heyski-emerald-aurora
description: Heyski Emerald Aurora — Travel / hospitality booking. Near-black dark-default with aurora emerald-violet wash confined to hero. Use when building interfaces that need this exact visual identity.
origin: superdesign
source: https://superdesign.dev/design-systems/heyski
---

# Heyski Emerald Aurora

> Enhanced from superdesign.dev&#x27;s Heyski study: dark-mode-default travel system with an aurora emerald-and-violet wash confined to the hero, glass-pill controls and warm photography cards.

- **Category:** Travel / hospitality booking
- **Mood:** Near-black dark-default with aurora emerald-violet wash confined to hero
- **Source:** superdesign.dev design-systems study (enhanced)

## When to use this skill

Load this design system when the product is a **travel / hospitality booking** and the brand voice is *near-black dark-default with aurora emerald-violet wash confined to hero*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #0c1210;          /* page canvas */
  --surface: #131c19;  /* cards, nav */
  /* ink */
  --ink: #eaf3ee;         /* headings */
  --ink-2: #b8cac2;      /* body */
  --muted: #87a297;     /* captions */
  --line: #22332c;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #34d399;
  --accent-soft: #132420;   /* tint backgrounds */
  --good: #34d399;
  --hot: #fb923c;         /* urgency only */
  /* radii */
  --r-s: 14px; --r-m: 20px; --r-l: 28px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `Outfit', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
| Body / UI | `Outfit', sans-serif` | Paragraphs, buttons, forms |

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
| 🏔️ | **200 resorts** | Alps, Dolomites, Caucasus |
| 🎫 | **Skip the queue** | Lift passes in your wallet app |
| 🎿 | **Gear delivered** | Fitted skis waiting at check-in |
| ❄️ | **Snow guarantee** | No snow, full refund |
