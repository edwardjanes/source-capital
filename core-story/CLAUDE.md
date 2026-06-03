# Source Capital Core Story — Change Log

## Files
- **source-capital-core-story.html** — Main presentation file (updated)
- **source-capital-core-story-backup.html** — Backup copy created 2026-05-26
- **source-capital-logo.png** — Logo asset (required for image display)

## Changes Made

### Logo Display & Styling
- Fixed logo path references: changed from `/mnt/user-data/uploads/2.png` to `source-capital-logo.png`
- Hero section (line 886): Logo displays at 52px height with auto width
- CTA section (line 2441): Logo constrained with `max-width: 200px` to prevent horizontal stretching

### Slide 26 — The Full Map
- Replaced JavaScript template literal syntax with 7 hardcoded HTML rows (01-07)
- Updated grid column widths: `80px 1fr 1fr 220px` for proper proportions
- Each row includes: number (green), evidence description, Source Capital provides (green background), and outcome tag
- Removed duplicate slide 26 content that appeared at end of presentation

### Year Updates (2026-05-26)
- Line 929: Section label updated from "1996 – 2025" to "1996 – 2019"
- Line 934: Chart title updated from "1996 to 2025" to "1996 to 2019"

### Currency Standardization (2026-05-26)
- Line 2014: Changed "£57M+" to "$57M+"
- Line 2301: Changed "£4–5M" to "$4–5M" and "£7–9M" to "$7–9M"

## Known Constraints
- All inline CSS styling (no Tailwind or CSS modules)
- Images referenced with relative paths (must be in same directory as HTML)
- Supabase join type patterns use Array.isArray checks to avoid build errors

## Next Steps
- Push updated files to GitHub repo: https://github.com/edwardjanes/source-capital
- Verify presentation displays correctly in browser after any further changes
