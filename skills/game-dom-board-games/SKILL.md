---
name: game-dom-board-games
description: "DOM Board & Card Games — Board / card / puzzle / tycoon. CSS-grid boards, transform tokens, modal decisions, HUD strips. Use when building or reviewing 2D browser games in plain HTML/JS/CSS."
origin: vercel-games-suite
source: https://games-suite.vercel.app
---

# DOM Board & Card Games

> Board/card/puzzle games via DOM+CSS instead of canvas: CSS-grid tile boards (free click targets), absolutely-positioned tokens animated by CSS transitions, explicit turn state machine, decision modals, live HUD strips, multi-language dictionaries.

Derived from production 2D browser games (ZCode Grand Arcade suite). Reference bar: single self-contained `index.html`, zero external assets, runs offline, ships in one paste.

## When to use this skill

Load whenever the deliverable is a **playable 2D browser game** — arcade, board, card, puzzle, RPG or action — in plain HTML/JS/CSS. Pair with `hallmark` (UI audit) and `make-interfaces-feel-better` (micro-interactions outside the play field).

## Universal architecture rules (all 2D browser games)

1. **Single file.** One `index.html`: `<style>`, markup, `<script>`. No build step.
2. **Explicit state machine.** `const STATE={BOOT,MENU,PLAY,PAUSE,OVER}` + `setState(s)` handling enter/exit. Never branch game phase on scattered booleans.
3. **Delta-time loop.**
```js
let last=0;
function loop(t){ const dt=Math.min((t-last)/1000,.05); last=t;
  if(state===STATE.PLAY) update(dt);
  render(); requestAnimationFrame(loop); }
```
4. **Input abstraction.** Keyboard map + touch buttons feed ONE `action(name)` path. Rebindable.
5. **Versioned saves.** `save={v:2,…}`; migrate older versions upward; try/catch localStorage (private mode).
6. **Synthesized audio.** Oscillator SFX through WebAudio — zero files. Create context after first user gesture. Persisted mute toggle.
7. **i18n dictionary from day one.** All UI strings via `t(key)`; add languages for free later.
8. **Decisions are modals.** Buy? Draw? Settings? How-to-play? = in-page modal, never alert().
9. **One-tap restart.** GAMEOVER → rematch instantly; persist best score/session stats.
10. **Tuning constants block.** All speeds/prices/spawn-rates live in one commented CFG object at the top of the script.

## Signature components

| Component | Spec |
|---|---|
| HUD | Fixed strips (score left, actions right), updated via dirty flags |
| Modal | Overlay + panel + focus trap + Esc + scale-in animation |
| Toast | Bottom-center transient pickup/error messages |
| Tutorial | First-run contextual hints tracked in save (`seenHints`) |

## Do / Don't

**Do** ship mute, pause (`P`/`Esc`), restart · keep tuning in CFG · telegraph threats
**Don't** tie physics to frames · use emoji as canvas sprites · block main thread >8ms/frame

## Demo files

- [`demo.html`](demo.html) — **playable** micro-game implementing these rules
- [`diagram.svg`](diagram.svg) — architecture anatomy

## Reference patterns

| **BOARD** | CSS grid of tile divs | Click targets free; easy theming |
| **TOKENS** | absolute + transform move | CSS transitions animate movement |
| **TURNS** | roll→act→resolve→next FSM | No implicit turn flow |
| **UI** | Modals for every decision | Never alert()/confirm() |
