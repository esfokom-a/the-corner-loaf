# Testing log: The Corner Loaf by Ansah Frederick

This log supports [the audit I wrote of Ansah Frederick’s site](audit-of-ansah-frederick.md). His review of my implementation is in the [audit I received](https://github.com/AnsFredd/the-corner-loaf-redesign/blob/main/docs/ee02/audit-of-elvis-fosu.md).

Site: https://ansfredd.github.io/the-corner-loaf-redesign/
Source reviewed: github.com/ansfredd/the-corner-loaf-redesign @ 14e3a7a (19 Nov 2026)
Standard: WCAG 2.2 AA

Each entry records the location, observation and method. Screenshots are linked next to the results they show.

## Saturday 21 November 2026

### Source review and colour measurement

- Pre-order and contact forms | The two name fields and the email field have no `autocomplete` attribute. Each input has an associated label and the `required` attribute. The forms give no visible required-field instruction | source review and visual inspection
- Form field boundaries | The #e8ded1 border measures **1.33:1** against white and **1.09:1** against the #f1e7d8 pre-order panel. The white field fill measures **1.22:1** against that panel | CSS colour calculation. [Pre-order fields](screenshots/08-preorder-field-borders.png)
- Text contrast | Muted body text measured **4.82:1** on cream and **5.90:1** on white. Prices measured **6.70:1** and footer text **8.93:1** | CSS colour calculation
- Placeholder text | The lighter examples measured **2.85:1** on white. The visible field labels separately identify each input, so this was recorded as a lower-priority observation | CSS colour calculation and visual inspection

### Automated tools

- Whole page | **axe-core 4.10.2**: 0 violations, 42 passes, 7 "needs review" (hero text colour contrast, background behind a pseudo-element) | tool: axe
- Whole page, desktop Chrome | **WAVE: 0 errors, 4 contrast errors, 23 alerts** (all "very small text"), **AIM 8.4/10** | [Desktop WAVE summary](screenshots/13-wave-desktop-summary.jpg)
- Whole page, earlier narrower in-app Chromium view | WAVE: 0 errors, 4 contrast errors, 24 alerts (all "very small text"), AIM 8.4/10 | [Earlier WAVE summary](screenshots/01-wave-summary.jpg)
- Hero tagline, h1, description, "Place a Pre-Order" | WAVE compares these four elements against the solid page background without accounting for the photo or gradient. Its contrast view shows **1.44:1** for the tagline against #faf7f1. Hiding the photo confirmed a tagline contrast issue. The overlay over the page background gives the tagline **3.30:1** at the top of the hero | WAVE and colour calculation. [WAVE contrast detail](screenshots/02-wave-hero-contrast.jpg)
- Whole page | **Lighthouse 13.5.0** (Chrome DevTools, Chromium 157, mobile: Moto G Power, slow 4G, 9:04 AM GMT): **Accessibility 100**, 22 passed, 10 manual checks listed, 41 inapplicable | tool: Lighthouse → [Mobile Lighthouse report](screenshots/12-lighthouse-mobile-100.png)

### Keyboard (in-app browser)

- Pastries filter | Activating it from the keyboard updates the results and posts "Showing 3 pastry product listings in the weekly menu." | keyboard
- FAQ | Enter and Space open the questions and update `aria-expanded` | keyboard
- Mobile menu | Escape closes the menu | keyboard
- Pre-order on Ansah’s site | An empty submit triggered native validation and moved focus to the name field. A valid test order displayed a confirmation. Submitting only spaces in both fields then replaced that confirmation and left focus on the submit button. The handler writes the error into `#preorder-list.textContent` | keyboard and source review. [Whitespace-only pre-order error](screenshots/09-preorder-whitespace-error-wipes-order.jpg)

### Zoom, text size and reflow (in-app browser viewport emulation)

- 320×720 at default text size | no horizontal scroll (scrollWidth 320) or clipping | viewport emulation
- 320px + WCAG text-spacing override (line-height 1.5, letter 0.12em, word 0.16em, paragraph 2em) | no overflow or clipping. **1.4.12 passes** | text spacing
- 640px at 100% and 150% root font size | the bake-count badge fits | visual check
- 640px + root text **200%** | the day badge "3 Bakes"/"2 Bak…" is cut off by the card edge: badge right 379px vs card right 309px, `white-space:nowrap` inside `overflow:hidden` | text size → [Day badge at 200% text size](screenshots/10-text-200pct-badge-clipped.jpg)
- 375px phone + root text 200% | the brand name "The Corner Loaf" is `nowrap` and runs past the screen (page scrollWidth 384 > 375, "Loaf" cut off); the hamburger drops to a second row | text size → [Phone header at 200% text size](screenshots/11-phone-375-text-200pct-header.jpg)
- "Scheduled today" badge | stayed at 11px when the root font size increased to 200% | computed font size

### Structure (Chrome accessibility tree)

- Page structure | HTML declares `lang="en"`. The accessibility tree exposes banner, main, contentinfo and the “Main navigation” landmark | source and accessibility tree
- Weekly menu | Seven unnamed `article`s. The products use plain `div`s without list-item roles. Each category appears before its product heading and each price follows it | accessibility tree and source
- Heading names | With All Products active, the weekly menu has six distinct headings named "Chin Chin", one for each day from Monday through Saturday. A seventh appears in "Today's Scheduled Bakes" on the Saturday tested | count of heading nodes in Chrome's accessibility tree
- "Today's Scheduled Bakes" | the "Saturday" label is a loose generic after the heading text; the products are h4s inside a `status` live region | a11y tree

### Screen reader (NVDA 2026.3.1 + Google Chrome, browse mode, Speech Viewer)

- Page load | before any key press, NVDA read the Today's Scheduled Bakes live region as one run: "Chin Chin GH₵ 20.00 Scheduled todayButter Croissants GH₵ 18.00 Scheduled todayBanana Bread GH₵ 15.00 Scheduled today". The announcement omitted the section heading | screen reader
- Down Arrow through Monday | "heading level 3 Monday / Start the week fresh2 Bakes / graphic Freshly baked artisan bread / BREAD / heading level 4 Whole Wheat Loaf / GH₵ 28.00 / SNACK / heading level 4 Chin Chin / GH₵ 20.00 / heading level 3 Tuesday". The subtitle and bake count run together. NVDA reads "SNACK" immediately after the previous product's price without announcing a list-item boundary | screen reader
- Forms | "Your Name" is read as text, then "edit required Enter your name". `required` is announced and the labels are read | screen reader
- Pre-order, valid submit (focus mode) | the confirmation was announced as one run: "Test 2 loaves Your pre-order request has been added successfully." | screen reader
- Pre-order, spaces-only submit | NVDA said only "Please complete all required fields before submitting." It didn't name a field, focus stayed on the button, and the loss of the earlier confirmation wasn't announced | screen reader

## Follow-up reported 22 November 2026

- FAQ | Elvis confirmed that a visible border marks the focused question when moving through the FAQ with Tab | keyboard
