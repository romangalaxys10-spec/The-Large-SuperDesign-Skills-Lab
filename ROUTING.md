# Skill routing — disambiguation for agents

Several skills in this lab cover adjacent concerns. When multiple match, use this
table to pick ONE per concern (stacking two skills that own the same layer
produces contradictory instructions — see Tony Lee's research notes in README).

## Minimal / clean aesthetics

| Situation | Load |
|---|---|
| Product keynote / launch deck | `keynote-clean-minimal` |
| SaaS landing page, restrained modern | `sd-confetti-minimal` or `linear-near-black-indigo` |
| Personal portfolio, quiet editorial | `awesome-minimal`, `warm-frame-chestnut` |
| Taste variance control instead of fixed identity | `taste-skill/taste-skill-v1` |

## Editorial / serif voices

| Situation | Load |
|---|---|
| Law firm / professional counsel | `legalline-paper-editorial` (fixed identity) |
| Culture talks, quote slides | `editorial-quote-serif` (slides) |
| Generic magazine style web page | `awesome-editorial` |
| Long-form AI research product | `anthropic-cream-grotesque` |

## Dark engineering identities

| Situation | Load |
|---|---|
| Dev SaaS / issue tracking | `linear-near-black-indigo` |
| Data platform / OLAP | `voltage-clickhouse-yellow` |
| Electronics repair lab | `techfix-blueprint-terminal` |
| Auto garage / performance | `autopro-voltage-dark` |
| No fixed identity — want data-driven recommendation | `pro-ui-ux-pro-max --design-system` |

## Brutalist family

| Situation | Load |
|---|---|
| Raw anti-design web aesthetic | `awesome-brutalism` |
| Refined neo-brutalist (thicker, playful) | `awesome-neobrutalism` |

## Games

Always: `game-fundamentals-2d` first → genre skill (`game-dom-board-games`
or `game-arcade-action` or `game-rpg-quest-worlds`) → `game-canvas-rendering`
→ finish with `game-feel-polish`.

## Review & quality gates (layer on top, never stack two)

| Concern | Load |
|---|---|
| Anti-AI-slop audit / redesign / study | `hallmark` (58 gates + self-critique) |
| Web design review checkpoints | `vercel-agent-skills/web-design-guidelines` |
| Accessibility + theming sweep | `frontend-design-anthropic` baseline |
| Micro-interaction pass (run LAST) | `make-interfaces-feel-better` |
