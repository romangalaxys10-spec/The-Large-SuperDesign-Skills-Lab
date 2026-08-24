---
name: game-rpg-quest-worlds
description: "RPG Quests & Tile Worlds — RPG / adventure / exploration. ASCII tilemaps, quest flags, typewriter dialogs, gentle economies. Use when building or reviewing 2D browser games in plain HTML/JS/CSS."
origin: vercel-games-suite
source: https://games-suite.vercel.app
---

# RPG Quests & Tile Worlds

> Top-down RPG craft: ASCII-string tilemaps (editable in notepad), camera follow, interaction radius, dialog queue with typewriter text and branch flags, inventory+gold, quest lifecycle available→active→done, forward-compatible saves.

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

| **WORLD** | ASCII string tilemaps | Legend const; edit in notepad |
| **DIALOG** | queue + typewriter + flags | Flags gate branches |
| **QUESTS** | available→active→done | Journal UI reads flag store |
| **ECON** | gold sources vs sinks table | Balance against income/minute |
