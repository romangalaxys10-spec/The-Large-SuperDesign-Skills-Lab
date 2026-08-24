# 🧪 The Large SuperDesign Skills Lab

**71 loadable design-system skills for AI coding agents.**
Each skill teaches an agent one complete visual identity — tokens, typography, layout grammar, components and guardrails — plus a live demo page and a token-anatomy diagram.

| | |
|---|---|
| 🟢 **Production Vercel systems** | 20 skills reverse-engineered from real, revenue-grade demos ([rommark.dev gallery](https://rommark.dev/)) |
| 🔵 **SuperDesign studies** | All **45 published systems** from [superdesign.dev/design-systems](https://superdesign.dev/design-systems), re-tokenized and enhanced |
| 🟡 **Presentation & slide systems** | 6 skills covering keynotes, consulting decks, pitch decks, editorial quotes, data-viz and workshop slides |
| 📦 **Per skill you get** | `SKILL.md` (agent instructions) · `demo.html` (working reference) · `diagram.svg` (visual token anatomy) |

Built by [Rommark.dev](https://www.rommark.dev) · MIT licensed

---

## 📖 Table of contents

1. [What is a design skill?](#-what-is-a-design-skill)
2. [Repository structure](#-repository-structure)
3. **[How agents should use these skills](#-how-agents-should-use-these-skills)** ← start here if you're an agent
4. [Agent installation per tool](#-agent-installation-per-tool)
5. [The skill selection matrix](#-skill-selection-matrix)
6. [The standard build workflow](#-the-standard-build-workflow)
7. [SKILL.md anatomy](#-skillmd-anatomy)
8. [Writing a new skill into this lab](#-writing-a-new-skill-into-this-lab)
9. [Full skill index](#-full-skill-index)
10. [Credits & license](#-credits--license)

---

## 🔬 What is a design skill?

A **design skill** is not a theme and not a template. It is a *set of instructions an AI agent can follow to reproduce a specific visual identity in any project*.

A good design skill answers four questions deterministically:

| Question | Where it's answered |
|---|---|
| *Which colors are allowed?* | CSS custom-property token block |
| *Which fonts, at which sizes?* | Typography table + fluid `clamp()` scale |
| *How is the page assembled?* | Layout grammar (numbered, ordered rules) |
| *When must the agent refuse a choice?* | Do / Don't guardrails |

Because each skill here was derived from either a **live production website** or a **published design.md study**, the tokens are proven — they already ship.

---

## 📁 Repository structure

```
The-Large-SuperDesign-Skills-Lab/
├── README.md                     ← you are here
├── index.html                    ← visual gallery: all 65 diagrams, open locally
├── skills-index.json             ← machine-readable index for agent discovery
├── LICENSE                       ← MIT
└── skills/
    ├── aquafix-hydro-ledger/
    │   ├── SKILL.md              ← THE SKILL — agent-loadable instructions
    │   ├── demo.html             ← standalone reference site (open in browser)
    │   └── diagram.svg           ← palette / type-scale / component anatomy
    ├── autopro-voltage-dark/
    │   ├── SKILL.md
    │   ├── demo.html
    │   └── diagram.svg
    ├── …  (65 folders total)
    └── sd-linear/
        └── …
```

### File contract inside every skill folder

| File | Purpose | Agent reads it when… |
|---|---|---|
| `SKILL.md` | YAML frontmatter + full instructions | Deciding whether the skill applies, and while writing UI code |
| `demo.html` | Self-contained single-file demo | It needs to see concrete markup patterns to imitate |
| `diagram.svg` | Rendered token anatomy | Explaining the system to a human, or sanity-checking contrast |

---

## 🤖 How agents should use these skills

This section is written **to the agent**. If you are an AI coding assistant (ZCode, Claude Code, Cursor, Codex, Antigravity, Copilot Workspace…), follow this exactly.

### Step 0 — Discover

Read [`skills-index.json`](skills-index.json). Each entry gives you:

```json
{
  "slug": "ironforge-volt-industrial",
  "name": "IronForge Volt Industrial",
  "origin": "vercel",                 // vercel = production-proven, superdesign = study-based
  "category": "Fitness / athletic club",
  "dark": true,
  "accent": "#e8ff47"
}
```

Pick candidates by matching the user's product domain against `category`, and their taste (`dark` vs light, accent hue) against the palette.

### Step 1 — Load exactly ONE skill

Open `skills/<chosen-slug>/SKILL.md`. Read it fully before writing any UI code.

> ⚠️ **Never mix two skills in one project.** One project = one identity. If the user asks for "X but with Y's colors", that is a new fork — copy the closer skill and change only the token block, then note the deviation in your summary.

### Step 2 — Apply tokens BEFORE components

Paste the `:root { … }` block from the skill into the project stylesheet first. Every later rule must reference `var(--…)`, never raw hex values. This is what makes the identity portable and re-skinnable.

### Step 3 — Follow the layout grammar in order

Every SKILL.md contains a numbered layout grammar (nav → hero → sections → footer). Build sections in that order. The grammar encodes decisions like:

- where gradients are allowed (usually hero only)
- section rhythm (typically `padding: 92px 0`, max-width 1200px)
- how many CTAs the hero may have (max two)

### Step 4 — Obey the guardrails

The **Do / Don't** table is binding:

- ❌ Never introduce a second accent hue
- ❌ Never place the accent color on large background areas unless the skill defines a media surface
- ❌ Never add font families beyond the two listed
- ✅ Use tabular numerals for prices/metrics
- ✅ Keep hover states as translateY lifts with shadow

If a user request conflicts with a guardrail, warn once, then do what the user says — but keep the violation isolated in the token block so it can be reverted.

### Step 5 — Verify against the demo

Before declaring done, open `demo.html` (or read its source) and diff your output mentally against three things:

1. Hero composition matches the grammar
2. Accent pixels ≤ ~10% of any viewport
3. Type scale steps match the clamp() values

### Worked example prompt

> *"Build me a landing page for my crossfit gym."*

Agent reasoning path:

```
skills-index.json → category "Fitness / athletic club"
                  → ironforge-volt-industrial (accent #e8ff47, dark)
load skills/ironforge-volt-industrial/SKILL.md
apply :root tokens → build nav/hero/classes/pricing per grammar
guardrails: acid-lime only on CTAs & energy words; Archivo Black uppercase display only
verify vs demo.html → done
```

### Multi-page consistency

For sites larger than a landing page: reuse the same token block on every page, and derive new sections only from the signature-component table in SKILL.md. Need a component the skill doesn't define (e.g., a pricing toggle)? Style it using only existing tokens — never invent new colors.

---

## 🔧 Agent installation per tool

<details>
<summary><b>ZCode</b></summary>

Clone the lab, then register the whole folder as a skill source:

```bash
git clone https://github.com/romangalaxys10-spec/The-Large-SuperDesign-Skills-Lab.git ~/.zcode/skills-lab
```

Point your agent at `~/.zcode/skills-lab/skills-index.json` for discovery, or symlink individual skills:

```bash
ln -s ~/.zcode/skills-lab/skills/ironforge-volt-industrial ~/.zcode/skills/design-ironforge
```

Then say: *"use the design-ironforge skill"*.
</details>

<details>
<summary><b>Claude Code / Codex CLI</b></summary>

Copy any skill folder into the project as `SKILL.md` conventions expect:

```bash
git clone https://github.com/romangalaxys10-spec/The-Large-SuperDesign-Skills-Lab.git
cp -r The-Large-SuperDesign-Skills-Lab/skills/aquafix-hydro-ledger .claude/skills/
```

Claude Code auto-discovers `.claude/skills/*/SKILL.md`.
</details>

<details>
<summary><b>Cursor / any MCP-less IDE agent</b></summary>

Add to `.cursorrules` / rules file:

```
DESIGN SYSTEM: When building UI, first read docs/skills/<slug>/SKILL.md and obey its
tokens, layout grammar and guardrails. Never use hex values outside the token block.
```

Keep the repo cloned next to the project.
</details>

<details>
<summary><b>Any LLM without file access</b></summary>

Paste a whole SKILL.md into the system/context window. At ~2–4 KB of prose + tokens, every skill fits comfortably alongside a task description.
</details>

---

## 🗺️ Skill selection matrix

Fast routing from product type → recommended skill(s):

| Product | First choice | Alternates |
|---|---|---|
| Plumbing / trades / emergency services | `aquafix-hydro-ledger` | `sd-teal-ledger-corporate` |
| Auto garage / performance | `autopro-voltage-dark` | `voltage-clickhouse-yellow` |
| Beauty salon / spa / aesthetics | `glowup-fraunces-atelier` | `warm-frame-chestnut` |
| Real estate / property investment | `sakartvelo-forest-gold-realty` | `teal-corporate-gradient` |
| Dental / medical clinic | `dentacare-clinical-mint` | `heyski-emerald-aurora` |
| Law firm / consultancy | `legalline-paper-editorial` | `anthropic-cream-grotesque` |
| Cleaning / facility services | `cleanpro-gambetta-eco` | `sd-confetti-minimal` |
| Gym / athletic club | `ironforge-volt-industrial` | `autopro-voltage-dark` |
| Bakery / café / food | `sweetest-warm-bakery` | `glowup-fraunces-atelier` |
| Electronics repair / technical | `techfix-blueprint-terminal` | `terminal-cyan-ledger-dark` |
| Dev SaaS / issue tracking | `linear-near-black-indigo` | `sd-framer`, `sd-cursor` |
| Fintech / money apps | `wise-ultra-black-lime` | `terminal-cyan-ledger-dark` |
| AI research / long-form product | `anthropic-cream-grotesque` | `sd-stack-ai` |
| Consumer hardware retail | `apple-flat-retail-light` | `sd-appscale-*` |
| Creative agency | `cream-island-violet-media` | `warm-frame-chestnut` |
| Developer infra / DB | `sd-neon-db`, `sd-planetscale`, `sd-supabase` | `terminal-cyan-ledger-dark` |
| OLAP / data platform | `voltage-clickhouse-yellow` | `sd-chrome-void` |
| Travel / booking | `heyski-emerald-aurora` | `sd-railway` |
| Personal portfolio | `warm-frame-chestnut` | `sd-minimalist-electric-cyan-portfolio` |

---

## 🏗️ The standard build workflow

```
user brief
   │
   ▼
① DISCOVER ── read skills-index.json, shortlist by category + mood
   │
   ▼
② LOAD ────── read chosen skills/<slug>/SKILL.md completely
   │
   ▼
③ TOKENIZE ── paste :root block into project CSS; forbid raw hex after this point
   │
   ▼
④ BUILD ───── assemble sections strictly in layout-grammar order;
              reuse signature components; respect radii/shadow scales
   │
   ▼
⑤ GUARDRAILS─ check Do/Don't list; isolate any user-requested deviations in tokens
   │
   ▼
⑥ VERIFY ──── compare against demo.html + diagram.svg
   │          (accent ratio ≤10%, type scale exact, spacing rhythm ≥92px)
   ▼
done ✔
```

---

## 🧬 SKILL.md anatomy

Every SKILL.md follows this fixed schema (so agents can parse them uniformly):

```markdown
---
name: <slug>
description: <one-line>            ← used for discovery/routing
origin: vercel | superdesign
source: <url>
---

# Name
> Mood description

## When to use this skill           ← routing conditions
## Design tokens                    ← :root CSS block (single source of truth)
## Typography                       ← display/body table + fluid scale
## Layout grammar                   ← numbered assembly order
## Signature components             ← button/card/chip/stat/testimonial specs
## Do / Don't                       ← binding guardrails
## Demo files                       ← links to demo.html & diagram.svg
## Reference features               ← example content pattern
```

---

## ✍️ Writing a new skill into this lab

Contributions welcome. Rules to keep the lab uniform:

1. Derive from a **real site** or a published design.md — no invented palettes.
2. Keep the exact SKILL.md schema above.
3. Token names are fixed: `bg surface ink muted line accent accent2 soft hot good`.
4. Generate `demo.html` as a self-contained single file (Google Fonts `<link>` allowed).
5. Include `diagram.svg`: 960×600, palette row, type scale, component specimens.
6. Add the entry to `skills-index.json`.

---

## 🗂️ Full skill index

Machine-readable: [`skills-index.json`](skills-index.json)
Visual: open [`index.html`](index.html) locally.

### 🟢 Production Vercel systems (20)

| Skill | Category | Live reference |
|---|---|---|
| [aquafix-hydro-ledger](skills/aquafix-hydro-ledger/SKILL.md) | Emergency plumbing services | [aquafix-sandy.vercel.app](https://aquafix-sandy.vercel.app) |
| [autopro-voltage-dark](skills/autopro-voltage-dark/SKILL.md) | Automotive workshop | [autopro-pi.vercel.app](https://autopro-pi.vercel.app) |
| [glowup-fraunces-atelier](skills/glowup-fraunces-atelier/SKILL.md) | Beauty atelier | [glowup-bice.vercel.app](https://glowup-bice.vercel.app) |
| [sakartvelo-forest-gold-realty](skills/sakartvelo-forest-gold-realty/SKILL.md) | Real estate investment | [sakartvelo-homes.vercel.app](https://sakartvelo-homes.vercel.app) |
| [dentacare-clinical-mint](skills/dentacare-clinical-mint/SKILL.md) | Dental clinic | [dentacare-hazel.vercel.app](https://dentacare-hazel.vercel.app) |
| [legalline-paper-editorial](skills/legalline-paper-editorial/SKILL.md) | Corporate law | [legalline.vercel.app](https://legalline.vercel.app) |
| [cleanpro-gambetta-eco](skills/cleanpro-gambetta-eco/SKILL.md) | Eco cleaning services | [cleanpro-snowy-sigma.vercel.app](https://cleanpro-snowy-sigma.vercel.app) |
| [ironforge-volt-industrial](skills/ironforge-volt-industrial/SKILL.md) | Athletic club | [ironforge-bice.vercel.app](https://ironforge-bice.vercel.app) |
| [sweetest-warm-bakery](skills/sweetest-warm-bakery/SKILL.md) | Artisan bakery | [sweetest-house.vercel.app](https://sweetest-house.vercel.app) |
| [techfix-blueprint-terminal](skills/techfix-blueprint-terminal/SKILL.md) | Electronics repair lab | [techfix-five.vercel.app](https://techfix-five.vercel.app) |

*(+10 curated editions of the studies below with hand-tuned tokens)*

### 🟡 Presentation & slide systems (new)

Slide-deck skills — each SKILL.md covers projection typography (32px back-row law), deck assembly grammar, layout patterns and chart rules; each demo.html renders an actual browsable deck:

| Skill | Category | Accent |
|---|---|---|
| [keynote-clean-minimal](skills/keynote-clean-minimal/SKILL.md) | Product launches / keynotes | ![#2997ff](https://img.shields.io/badge/2997ff-%232997ff) |
| [mckinsey-consult-deck](skills/mckinsey-consult-deck/SKILL.md) | Consulting / board decks | ![#2251ff](https://img.shields.io/badge/2251ff-%232251ff) |
| [pitch-dark-startup](skills/pitch-dark-startup/SKILL.md) | Startup fundraising | ![#6ee7b7](https://img.shields.io/badge/6ee7b7-%236ee7b7) |
| [editorial-quote-serif](skills/editorial-quote-serif/SKILL.md) | Culture talks / quotes | ![#b08d57](https://img.shields.io/badge/b08d57-%23b08d57) |
| [dataviz-standard-pro](skills/dataviz-standard-pro/SKILL.md) | Analytics reviews / data-viz | ![#0072b2](https://img.shields.io/badge/0072b2-%230072b2) |
| [workshop-facilitator-pop](skills/workshop-facilitator-pop/SKILL.md) | Workshops / training rooms | ![#ffd60a](https://img.shields.io/badge/ffd60a-%23ffd60a) |

## 🔵 SuperDesign studies — all 45 systems

`sd-*` prefixed skills map 1:1 to https://superdesign.dev/design-systems:
ai-builder-club · anthropic · apple · appscale-premium-apps-and-hosting-store · atelier-reveal-or-pomodoro · calcom · chrome-void · clay · claymorphic-comic-ledger · confetti-minimal · cream-island (+variant) · cursor · faceted-plum-institutional · fieldwork-grotesk · framer · frequency-based-extraction · global-enterprise-intelligence-design-system · heyski · intelligence-ai · lenisdev · linear · minimalist-electric-cyan-portfolio · my-design-system (+variant) · neon-db · planetscale · railway · ration-blue-gate-card · rationed-aurora-light · rationed-voltage-dark · scriptforge-ai-11-reference-match · stack-ai · supabase · teal-ledger-corporate · terminal-cyan-ledger · the-modern-scholar · traceso · vapi-ai · viktor · violet-ledger-interface · void-teal-ledger-glass · warm-frame-portfolio-light · wdi · wise

Plus 10 curated editions: `linear-near-black-indigo` · `wise-ultra-black-lime` · `anthropic-cream-grotesque` · `apple-flat-retail-light` · `cream-island-violet-media` · `terminal-cyan-ledger-dark` · `teal-corporate-gradient` · `warm-frame-chestnut` · `voltage-clickhouse-yellow` · `heyski-emerald-aurora`

---

## 🙌 Credits & license

- **SuperDesign-derived skills** credit [superdesign.dev/design-systems](https://superdesign.dev/design-systems) — the source studies.
- **Vercel-family designs** are original works crafted by [Rommark.dev](https://www.rommark.dev).
- Code samples MIT — see [LICENSE](LICENSE). Visual identities remain the property of their respective brands; use the skills to learn structure, don't impersonate brands.

<div align="center">
<b>Crafted by <a href="https://www.rommark.dev">Rommark.dev</a></b><br>
<sub>The Large SuperDesign Skills Lab — teach your agent taste.</sub>
</div>
