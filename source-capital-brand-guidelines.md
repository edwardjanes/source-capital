# Source Capital — Brand Guidelines
> For use by LLMs and contractors when producing any visual or written content for Source Capital.
> v2.0 — 9 September 2026. Supersedes the previous dark-first "Electric Green / Pitch Black" version of this file, which is retired as of the site rebuild.

---

## 1. Brand Overview

**Company:** Source Capital
**Website:** sourcecapital.co.uk
**Positioning:** Approachable mentor. Investment advisory and consultancy for founders raising pre-seed/seed capital ($250k–$1M). Dubai-based, globally operating.
**Brand character:** Direct, warm, earned confidence, plain-spoken, honest. Authority comes from having actually done the raise — not from gatekeeping, exclusivity, or hype. Not an untouchable insider club. Not a black-box "we guarantee results" machine.

---

## 2. Colour Palette (light system — current)

| Role | Hex | Usage |
|---|---|---|
| Primary green (brand accent) | `#2AF76F` | CTAs, highlights, icons, small UI accents. NOT body text — fails contrast on white. |
| Deep green (text/CTA/active-state accent) | `#0E7231` | Inline links, active nav state, primary CTA fills, focus outlines. Measures 6.05:1 on white (AA). |
| Deep green — hover | `#0A5C28` | Hover state for anything filled with `#0E7231`. |
| Pale mint (tints only) | `#B4FAD1` | Backgrounds, card tints, subtle highlights. Never text. |
| Grey (body copy) | `#585858` | Default body text on white. Measures 7.11:1 (AA). |
| Off-white (section surface) | `#F7FAF8` | The one section/card background tint used sitewide — do not introduce another off-white. |
| Black | `#000000` | Headlines / high-contrast moments only. |
| White | `#FFFFFF` | Default background — this is a LIGHT, white-background brand system. |

**Rules:**
- Default layout is light (white background), not dark. Dark UI elements (buttons, hover states) use `#0E7231`, not pitch black.
- `#2AF76F` on white fails WCAG AA for text — use only for large/bold elements, or pair with `#0E7231`/black backgrounds. Never use it as a hover *border* color on its own — it measures 1.44:1, below the 3:1 minimum for non-text UI; pair it with a second signal (shadow, fill, weight) or use `#0E7231` instead.
- `#128A3D` (the previous deep-green token) is **retired** — it measured 4.44:1 on white, just under the 4.5:1 AA minimum for text, and was used as the site's primary link/CTA/active-nav color. Corrected to `#0E7231` sitewide 9 Sep 2026 (design review finding H1). Do not reintroduce `#128A3D` for text or CTA fills.
- Maintain WCAG AA contrast throughout: 4.5:1 minimum for text, 3:1 minimum for non-text UI (borders, focus rings, icons that convey state).
- Never remove a focus indicator (`outline: none`) without a same-or-better-visibility replacement.

## 3. Voice & Tone

**Use:** raise, round, founders, investors, traction, the ask, the room — plain fundraising vocabulary.
**Avoid:** "smart money," "unicorn factory," "guaranteed to close," "leverage synergies," or any absolute promise about raise outcomes.

| Attribute | What it means | What it isn't |
|---|---|---|
| Direct | Gets to the point fast | Curt or cold |
| Warm | Talks like a person | Overfamiliar |
| Earned confidence | Speaks from having done the raise | Arrogant or gatekeeping |
| Plain-spoken | Translates jargon into what it means | Dumbed-down |
| Honest | Names the real problem | Harsh or discouraging |

## 4. Typography

Clean geometric sans-serif (Inter or similar). Minimum body size 16px web.

## 5. Imagery

Real, human imagery over generic stock — founders, real conversations. Avoid the "exclusive insider club" cliché (closed doors, staged boardrooms).

---

*Full sourcing/rationale for these decisions lives in the Source Capital project's "Brand Guidelines" doc (v1.0, 3 Sep 2026) and the site-architecture-plan.md. This file is the condensed, build-ready reference for anyone (human or LLM) producing pages directly in this repo.*
