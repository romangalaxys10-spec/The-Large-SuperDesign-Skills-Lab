---
name: terminal-cyan-ledger-dark
description: Terminal Cyan Ledger Dark — Developer tools / infrastructure. Monospace ledger with cyan ink on true black. Use when building interfaces that need this exact visual identity.
origin: superdesign
source: https://superdesign.dev/design-systems/terminal-cyan-ledger
---

# Terminal Cyan Ledger Dark

> Enhanced from superdesign.dev&#x27;s Terminal Cyan Ledger: monospace-led ledger UI, cyan-on-black contrast pairings, tabular numerals everywhere and status colors borrowed from terminal semantics.

- **Category:** Developer tools / infrastructure
- **Mood:** Monospace ledger with cyan ink on true black
- **Source:** superdesign.dev design-systems study (enhanced)

## When to use this skill

Load this design system when the product is a **developer tools / infrastructure** and the brand voice is *monospace ledger with cyan ink on true black*. Apply the tokens verbatim before writing any component CSS.

## Design tokens

```css
:root {
  /* surfaces */
  --bg: #000000;          /* page canvas */
  --surface: #0c1116;  /* cards, nav */
  /* ink */
  --ink: #e6ffff;         /* headings */
  --ink-2: #a1b9c0;      /* body */
  --muted: #5c7382;     /* captions */
  --line: #16202a;       /* hairlines & borders */
  /* accent — RATIONED: CTAs, active states, data highlights only */
  --accent: #00e5cc;
  --accent-soft: #07211f;   /* tint backgrounds */
  --good: #3fd68f;
  --hot: #ff5c5c;         /* urgency only */
  /* radii */
  --r-s: 4px; --r-m: 8px; --r-l: 12px;
}
```

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / headings | `JetBrains Mono', sans-serif` | Hero + section titles, tight tracking (-0.02em to -0.04em) |
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
| 📊 | **Unit economics** | Cost per request, auto-tagged |
| 🚨 | **Anomaly alerts** | Slack ping before finance asks |
| 🧾 | **Showback reports** | Team-level monthly ledgers |
| 🔗 | **Provider sync** | AWS, GCP, Vercel in minutes |
