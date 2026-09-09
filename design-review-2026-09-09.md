# Design Review — sourcecapital.co.uk

**Reviewed:** 9 September 2026
**Scope:** Live site pages under `source-capital/` (home, services ×5, about, contact, how-it-works, resources, terms, privacy, redirect stubs). `legacy/`, the core-story decks, and the `raise-velocity-*` onboarding files were excluded.
**Method:** Apple HIG design principles (accessibility, colour, typography, layout, writing, entering-data, branding), checked against `source-capital-brand-guidelines.md` v2.0.

---

## Summary

**Rating: Needs Work — with one Critical blocker.**

The underlying design system is sound: a clear light/white brand, a single readable body grey at 7.1:1, a sensible four-tier information architecture, and shared nav/footer partials that keep pages consistent. The writing is genuinely good — direct, plain-spoken, and on-brand.

But the site is not shippable in its current state. **`/how-it-works/` renders an empty page** — the R.A.I.S.E. framework content that the CSS, the nav, the homepage and the services page all point at simply isn't in the document. **There is no mobile navigation at all.** Placeholder copy is live on the homepage and resources page. And Terms and Privacy are still on the retired black brand.

Underneath that, the recurring theme is a green that doesn't quite carry its weight: `#128A3D` lands at 4.44:1 on white — just under AA — and it's the colour of every inline link and the primary CTA. The brand file asserts this pairing is safe; it isn't, by a small margin.

---

## Critical Issues

### C1. `/how-it-works/` has no content
**What:** `how-it-works/index.html` defines ~40 CSS rules for `.pipeline`, `.step-btn`, `.card`, `.progress-fill` — an interactive five-step R.A.I.S.E. walkthrough — but the `<body>` contains only the nav, two lines of text, and the footer (50 lines total, zero references to any of those classes). The page has no `<h1>`.

**Why:** *Design Guideline — Layout*: "Make essential information easy to find by giving it sufficient space." A page reachable from the primary nav, the homepage ("See the Full Framework →"), and the services hero must contain the thing it promises. This is also the only page on the site with no `<h1>`.

**Fix:** Restore the framework markup. The CSS is intact, so this is markup + the step data, not a redesign. Until it's restored, either the nav item or the page should be pulled — three separate CTAs currently lead to a dead end.

---

### C2. No mobile navigation
**What:** `_partials/nav.html` hides the entire link set below 768px (`.sc-nav-links { display: none }`) and provides no replacement — no menu button, no drawer, no bottom bar. On a phone the header is: logo, and "Book a Call". Services, How It Works, About, Resources and Contact are unreachable from any page except by scrolling to a body link that happens to exist.

**Why:** *Design Guideline — Layout / Accessibility (Intuitive)*: "Your interface uses familiar and consistent interactions that make tasks straightforward to perform." Hiding primary navigation with no alternative isn't responsive design; it's removal.

**Fix:** Add a menu toggle in the same partial (so it propagates via `scripts/sync-partials.py`):
```html
<button id="scNavToggle" aria-expanded="false" aria-controls="scNavLinks"
        aria-label="Menu"
        style="display:none;width:44px;height:44px;border:0;background:none;">☰</button>
```
```css
@media (max-width: 767px) {
  #scNavToggle { display: flex !important; align-items:center; justify-content:center; }
  .sc-nav-links { display: none; }
  .sc-nav-links.open {
    display: flex; flex-direction: column; gap: 4px;
    position: absolute; top: 100%; left: 0; right: 0;
    background: #fff; border-bottom: 1px solid #eee; padding: 8px 24px 20px;
  }
  .sc-nav-links.open a { padding: 12px 0; }   /* 44px targets */
}
```
Toggle `.open` and `aria-expanded` on click; close on Escape and on link activation.

---

### C3. Focus indicator removed from every form field
**What:** `contact/index.html`:
```css
input:focus, textarea:focus { outline: none; border-color: var(--brand-green); }
```
`#2AF76F` measures **1.44:1** against the white page and **1.02:1** against the `#d9d9d9` border it replaces. The focus state is effectively invisible.

**Why:** *Design Guideline — Accessibility (Speech / Mobility)*: "Let people use the keyboard alone to navigate and interact with your app… ensure your interface elements are appropriately labeled." A keyboard user cannot tell which field they are in. Non-text UI indicators need 3:1.

**Fix:** Never `outline: none` without a replacement of equal or better visibility:
```css
input:focus-visible, textarea:focus-visible {
  outline: 2px solid #0E7231;      /* 6.05:1 on white */
  outline-offset: 2px;
  border-color: #0E7231;
}
```
Add the same treatment site-wide for links and buttons — no page currently defines any `:focus` style except this one.

---

### C4. Contact form has no labels
**What:** All four fields are placeholder-only: `<input type="text" name="name" placeholder="Name" required>`. No `<label>`, no `aria-label`.

**Why:** *Design Guideline — Writing*: "If your app allows people to enter their own text… **label all fields clearly**, and use hint or placeholder text so people know how to format the information." Placeholders vanish on first keystroke, are announced inconsistently by screen readers, and render at low contrast by default.

**Fix:** Add visible labels above each field and keep placeholders as format hints:
```html
<label for="cf-email" style="display:block;font-size:14px;font-weight:500;color:#000;margin-bottom:6px;">Email</label>
<input id="cf-email" type="email" name="email" placeholder="name@example.com" required>
```

---

### C5. Placeholder copy is live
**What:** Nine `[PLACEHOLDER — …]` blocks are rendered to visitors:
- `index.html:111` — the social-proof section (the block itself says *"Do not ship this numbers-only"*)
- `index.html:175` — an unanswered objection in "Before you book a call"
- `resources/index.html` — the subhead, the featured-resource description, and all three article cards

**Why:** *Design Guideline — Writing*: "Provide clear next steps on any blank screens… An empty screen can be daunting if it isn't obvious what to do next." Visible internal notes on a page whose entire job is establishing credibility with investors' founders does the opposite of that job.

**Fix:** Write the real content, or remove the sections. For Resources specifically, a short honest "Guides are being written — book a call in the meantime" beats three fake cards.

---

### C6. Terms and Privacy are on the retired brand
**What:** `terms.html` and `privacy.html` use `class="bg-black text-white"` with `text-emerald-400` links — the dark "Electric Green / Pitch Black" system the brand file explicitly retires ("*Default layout is light (white background), not dark*"). Neither page includes the nav or footer partial, and both link back with a relative `href="index.html"`. `text-emerald-400` isn't in the palette at all. Neither has a meta description.

**Why:** *Design Guideline — Branding*: "Help people feel comfortable by using standard patterns consistently." Every page's footer links here, so every visit can dead-end in a page that looks like a different company.

**Fix:** Rebuild both on the light template with the nav and footer partials, `#585858` body on white, `#0E7231` links, absolute `/` paths.

---

## Improvements

### H1. `#128A3D` on white misses AA by a hair — and it's everywhere
**What:** Measured **4.44:1**; AA for text under 18pt is 4.5:1. It's the colour of `.brand-accent` (every inline "→" link at body size), the active nav item at 14px, and — inverted — the white text on the primary green CTA button, which measures the same 4.44:1.

**Why:** *Design Guideline — Accessibility*: "Text sizeUp to 17 pts / All weights / **Minimum contrast ratio 4.5:1**." The brand file states this pairing maintains AA; it doesn't, marginally.

**Fix:** Darken the token to **`#0E7231`** — already in the codebase as the button hover colour, and it measures **6.05:1** on white. Swap `--brand-deep-green` to `#0E7231` for text and CTA fills, and pick a new darker hover. This one change fixes links, active nav, and the CTA in a single edit across every page. Worth correcting §2 of `source-capital-brand-guidelines.md` at the same time.

### H2. `text-gray-400` used for real copy — 2.54:1
**What:** Tailwind's `text-gray-400` is `#9ca3af` = **2.54:1** on white. Used 11 times across live pages: the tier-card eyebrow labels ("Do it yourself", "We do it with you"), the "No guarantees, no smart-money mythology" line, the resources card categories, and — worst — the contact form's status/error message.

**Why:** *Design Guideline — Accessibility*: 4.5:1 minimum. **Error messages must never be the least readable text on the page.** *Writing*: "Show errors right next to the field, and instruct people how to enter the information correctly."

**Fix:** Replace every `text-gray-400` with `text-[#585858]` (7.11:1). For the form status, use `#585858` for the neutral state and a dark red (`#B3261E`, 6.2:1) for the failure state.

### H3. Inter never loads
**What:** Every page declares `font-family: 'Inter', system-ui, sans-serif`, but there is no `<link>` to Google Fonts, no `@font-face`, and no font files in the repo. Confirmed across all 19 live pages.

**Why:** *Design Guideline — Branding*: "Consider using a custom font. If your brand is strongly associated with a specific font, be sure that it's legible at all sizes." Right now every visitor sees their OS default — SF Pro on Mac, Segoe UI on Windows, Roboto on Android. Line lengths, heading weights and the whole vertical rhythm differ per platform, and the brand's stated typeface is absent.

**Fix:** Either commit to Inter and load it in `_partials/analytics.html` (which is already injected into every `<head>`):
```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
```
…or drop `'Inter'` from the stacks and state in the brand file that the system font is the brand font. Silently naming a font you don't ship is the one option that helps nobody.

### H4. Form result isn't announced
**What:** On success the form is hidden and `#contact-form-status` text is swapped. There's no `aria-live`, so a screen-reader user gets silence — and the form they were filling disappears.

**Why:** *Design Guideline — Accessibility (Perceivable)*: "Your interface doesn't rely on any single method to convey information."

**Fix:** `<p id="contact-form-status" role="status" aria-live="polite">`, and move focus to it after submit.

### H5. Things that look clickable but aren't (and vice versa)
**What:** Two opposite problems:
- Homepage tier cards (`index.html`) have `.tier-card:hover { border-color: #2AF76F }` but contain no link — they respond to the pointer and do nothing.
- Resources placeholder cards are `<a href="#">` — real, focusable, screen-reader-announced links that navigate nowhere.

**Why:** *Design Guideline — Color*: "Avoid using the same color to mean different things… if you use your brand color to indicate that a borderless button is interactive, using the same or similar color to stylize noninteractive text is confusing."

**Fix:** Make the homepage tier cards links to their service pages (the services page already does this correctly with explicit buttons). Change the resources placeholders to `<div>` with `aria-disabled` styling until the posts exist.

### H6. Hover states are invisible
**What:** `.tier-card:hover` and `hover:border-[#2AF76F]` both set a 1px `#2AF76F` border — **1.44:1** against white.

**Why:** Non-text state indicators need 3:1 to be perceivable.

**Fix:** Use `#0E7231` for the hover border, or pair the colour with a second signal (border-width, a subtle shadow, a slight lift) — *Accessibility*: "Convey information with more than color alone."

---

## Medium

| # | Issue | Fix |
|---|---|---|
| M1 | **Three different off-whites** for section backgrounds: `bg-gray-50` `#f9fafb` (home), `bg-[#F7FAF8]` (about), `#f8f7f4` (how-it-works, a warm cream the retired brand explicitly prohibited). | Pick one — suggest `#F7FAF8` — and add it to the brand file as a named surface token. *Layout: "Group related items… use background shapes, colors."* |
| M2 | **Button radius drifts.** `rounded-full` for CTAs everywhere except About's "Read the Story ↓", which is `rounded-2xl`. | Standardise on `rounded-full` for actions. |
| M3 | **`profile.PNG` is 1.15 MB and loads twice on About**, at ~300–500px display width, with no `loading="lazy"` and no `width`/`height`. No image on the site has dimensions set. | Export a ~600px WebP (target <80 KB), set explicit `width`/`height` to stop layout shift, `loading="lazy"` on the second instance. |
| M4 | **Same image, same alt text, twice on one page** — a screen reader reads "Edward Janes, founder of Source Capital" twice in one document. | `alt=""` on the second (decorative) instance. |
| M5 | **`text-xs` (12px) carrying real copy** — the apply page's founder bio, the resources card descriptions. Brand file: "Minimum body size 16px web." | Raise to 14px minimum, 16px for anything that's a sentence. *Typography: "Use font sizes that most people can read easily."* |
| M6 | **Copy contradicts itself across pages.** The free audit is "30 minutes" (home, contact) and "20 Minutes" (apply, accelerator). The homepage says *"No guarantees, no smart-money mythology"*; the apply page has a section headed **"The guarantee"** promising 10 investor meetings or free work. The brand file bans "any absolute promise about raise outcomes." | Settle on one duration. Decide whether the guarantee is the offer or not — currently a visitor who reads both pages has caught you contradicting yourself on the page where they book. |
| M7 | **`services/raise-hq/` has no footer** — no Terms/Privacy/copyright on a page selling a product. | Run `scripts/sync-partials.py` against it. |
| M8 | **Redirect stubs have no `<meta name="viewport">`** (news, portfolio, events-page, business-dashboard, search-opportunities) — briefly renders desktop-zoomed on mobile. | Add the viewport tag to the stub template. |
| M9 | **No skip link** on any page. Keyboard users tab through six nav items on every page. | `<a href="#main" class="sr-only focus:not-sr-only">Skip to content</a>` in the nav partial; add `id="main"` to each page's first section. |
| M10 | **"Book a Call" nav button is ~36px tall** (`padding:10px 20px`, 14px text) — below the 44pt guidance, and on mobile it's the *only* control in the header. | `padding: 12px 20px` and `min-height: 44px`. *Accessibility: "mobile / default control size 44×44 pt."* |
| M11 | **Tailwind Play CDN in production** on 13 pages — a render-blocking script that compiles CSS in the browser on every visit. | Fine for prototyping; before launch, either build a static stylesheet or move to the inline-CSS approach `raise-hq` already uses. |

---

## Positive Notes

- **`services/raise-hq/index.html` is the best-built page on the site.** Self-contained CSS, `aria-selected` maintained on its tab set, `aria-label` on the carousel dots, buttons genuinely disabled at the ends of the track, passive touch listeners — and it is the **only** page that respects `prefers-reduced-motion`. Use it as the template for the others.
- **The partials system works.** `_partials/nav.html` / `footer.html` / `analytics.html` plus `scripts/sync-partials.py` means a nav or contrast fix is one edit, not nineteen. Both C2 and H1 are cheap because of this.
- **Body text is properly readable.** `#585858` on white at 7.11:1 clears AA comfortably, and 16px+ is the norm across body copy — better than most marketing sites.
- **The active-nav-state script** correctly handles the `/` vs `/index.html` edge case and prefix-matches sub-routes.
- **The writing is on-brand and genuinely good.** "None of that is a reason to give up on the raise. It's a reason to not do it alone." That's the brand file's "direct, warm, earned confidence" landing exactly as specified. *Writing: "Determine your app's voice… Consistent language, along with a voice that reflects your values, helps everything feel more cohesive."*
- **The four-tier IA is clear** and the same four tiers appear in the same order on home and services — good structural consistency.
- **Alt text is present on every image** across all 19 live pages, and it's descriptive rather than filename-dumped.

---

## Suggested Order of Work

**Before anything else ships:**
1. Restore `/how-it-works/` content (C1)
2. Add mobile navigation (C2)
3. Remove or write the placeholder copy (C5)
4. Rebuild Terms + Privacy on the light brand (C6)

**Accessibility pass — roughly half a day, mostly find-and-replace:**
5. `--brand-deep-green` → `#0E7231`, update the brand file (H1)
6. `text-gray-400` → `text-[#585858]`; red for errors (H2)
7. Restore focus indicators site-wide (C3)
8. Add form labels + `aria-live` (C4, H4)
9. Skip link, 44px nav button (M9, M10)

**Consistency and polish:**
10. Decide the Inter question (H3)
11. Fix false affordances and hover contrast (H5, H6)
12. One off-white, one button radius (M1, M2)
13. Reconcile 20 vs 30 minutes, and the guarantee (M6)
14. Compress and lazy-load images (M3, M4)
15. Footer on raise-hq, viewport on the stubs (M7, M8)
16. Replace the Tailwind CDN before launch (M11)

---

## A Note on Method

This review applied Apple HIG principles to a marketing website. Most transferred cleanly — contrast ratios, target sizes, focus indicators, labelling, writing, and colour consistency are platform-independent. A few HIG areas were not applicable and were skipped: safe areas, system colour tokens, launch screens, gestures, and dark mode (this brand is deliberately light-only, which is a legitimate choice — but note that `terms.html` and `privacy.html` currently ship a *de facto* dark mode by accident).
