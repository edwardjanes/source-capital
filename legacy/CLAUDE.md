# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**Source Capital – Raise Velocity** is a marketing and product materials collection for the premium done-for-you raise advisory service. The folder contains self-contained HTML presentations and onboarding materials, plus brand guidelines that apply to all content.

### File Structure

| File | Purpose |
|------|---------|
| `raise_velocity_onboarding_v5.html` | Interactive 12-week process timeline (3 phases: Setup, Outreach, Pitching). Click-to-reveal stage details with progress navigation. |
| `customer-journey.html` | Customer journey visualization showing founder touchpoints and outcomes. |
| `raise-velocity-onboarding.html` | Earlier version of onboarding content (reference/backup). |
| `source-capital-brand-guidelines.md` | **Read this first.** Complete brand rules, colour palette, typography, voice tone, and prohibitions. Applies to all visual/written content. |
| `Source Capital Core Story/source-capital-core-story.html` | 30+ slide narrative presentation covering market opportunity, Source Capital history, and value proposition. |
| `Source Capital Core Story/CLAUDE.md` | Changelog for core story edits (logo paths, slide updates, year/currency corrections). |

---

## Brand & Design Constraints

**Critical rules** (from `source-capital-brand-guidelines.md`):

- **Colours:** Electric Green `#00FF84` (accent only), Pitch Black `#000000` (background), Off-White `#E8E8E8` (text)
- **Typography:** Inter (headlines, weight 900, ALWAYS UPPERCASE) + Montserrat (body, regular weight)
- **Dark-first:** All layouts default to black backgrounds. Green is never a large background fill.
- **Logo:** Only use on dark backgrounds. Never recolour, stretch, or recreate. The "E" has two horizontal bars—preserve this.
- **Voice:** Direct, authoritative, outcome-focused, British English, no corporate filler.
- **Prohibited:** Warm colours, rounded/bubbly elements, gradients on logo, stock photography clichés, American spelling.

**When editing HTML files:** Ensure inline CSS respects these constraints. Update comments if colour values or brand elements change.

---

## Common Development Tasks

### Editing Onboarding Content (`raise_velocity_onboarding_v5.html`)

The file is a single-page HTML document with embedded CSS and JavaScript. Structure:

1. **Data layer** (line ~93): Array of phase objects (Setup, Outreach, Pitching), each with stages, titles, body text, and week assignments.
2. **Rendering** (line ~92+): JavaScript loops over `data` to build phase headers, stage lists, and detail cards.
3. **Interactivity:** Click a phase to expand it; click a stage to show its detail card.

**To add/edit a stage:**
1. Find the correct phase object in the data array (e.g., `setup`, `outreach`, `pitching`).
2. Add or modify a stage object: `{num:5, label:'...', week:'...', title:'...', body:'...', tick:0}`
3. The `tick` value is a progress indicator (0 = not started, increments for weeks).
4. The `num` field is auto-rendered as a numbered circle.

**To update styling:**
- Inline CSS is at the top (`<style>` tag). Classes like `.rv-card`, `.phase-header`, `.s-name` control layout and colours.
- Keep all colours aligned with the brand palette (green `#00FF84`, greys `#A0A0A0`, `#555`, `#1a1a1a`).
- Do not add external stylesheets or Tailwind.

### Editing the Core Story Presentation

Located in `Source Capital Core Story/source-capital-core-story.html`. Large single-page HTML with 30+ slides.

**Common updates:**
- **Slide content:** Search for the slide title (e.g., "The Full Map") and edit the HTML/text directly. Inline CSS controls layout.
- **Logo:** Ensure `<img src="source-capital-logo.png">` is used (not absolute paths like `/mnt/user-data/...`). Logo must be in the same folder.
- **Year/currency:** Use global find-and-replace for consistency (e.g., "1996 – 2025" → "1996 – 2019"; "£" → "$"). Update the CLAUDE.md changelog in the subdirectory after major changes.
- **Colors/typography:** Follow brand guidelines. Do not deviate.

**Building/Testing:**
- No build step required. Open the HTML file directly in a browser to verify changes.
- Test across desktop and mobile (responsive design uses flexbox and viewport meta tag).

---

## Brand Assets & Logos

- **Logo file:** `Source Capital Core Story/source-capital-logo.png` (1.7 MB, used in core story presentation).
- **Inline SVG logos:** Some HTML files embed logos as SVG `<text>` elements (e.g., `raise_velocity_onboarding_v5.html`, line 66). These render as "SOURCE" (green) + "CAPITAL" (off-white) wordmark. Do not modify letterforms.

---

## Key Constraints & Patterns

1. **Inline CSS only.** No CSS modules, Tailwind, or external stylesheets. All styling is in `<style>` tags.
2. **Self-contained HTML files.** Each file is a standalone document—no external JavaScript libraries except fonts from Google Fonts API.
3. **Responsive design via flexbox.** Layout adapts to mobile/tablet using flex properties and media queries (where present).
4. **Relative image paths.** Images referenced in HTML must be in the same directory or a relative path (e.g., `<img src="logo.png">` or `<img src="./subfolder/image.png">`).
5. **Progress/state management:** Data-driven. The phase/stage timeline in `raise_velocity_onboarding_v5.html` uses a JavaScript data array; edits to text/structure require updating the data object, not the DOM.

---

## Common Pitfalls

- ❌ **Adding external dependencies** (Bootstrap, Tailwind, libraries). Keep it inline.
- ❌ **Changing brand colours** without reading guidelines. Update the CLAUDE.md changelog if colour changes are approved.
- ❌ **Using absolute image paths** (e.g., `/mnt/user-data/...`). Always use relative paths.
- ❌ **Modifying logo letterforms or adding effects** (drop shadows, gradients, recolours). Logo is protected.
- ❌ **American English in copy.** Use British spelling (colour, optimised, cheque).

---

## Future Work

- **GitHub repo:** Core story and onboarding files may be pushed to https://github.com/edwardjanes/source-capital (verify before adding sensitive data).
- **Version control:** If stored in Git, commit messages should note brand/content changes (e.g., "Update timeline stages for Setup phase").
- **Browser testing:** Always open files in a browser after edits to verify rendering and interactivity.
