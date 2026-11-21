# Testing log: The Corner Loaf by Ansah Frederick

Site: https://ansfredd.github.io/the-corner-loaf-redesign/
Source reviewed: github.com/ansfredd/the-corner-loaf-redesign @ 14e3a7a (19 Nov 2026)
Standard: WCAG 2.2 AA

Each entry records the location, observation and method. Screenshots are linked next to the results they show.

## Saturday 21 November 2026

### Source review and colour measurement

- Weekly menu, every product | products use `<div>` elements. The category precedes the h4 and the price follows in a separate paragraph | source, Chrome accessibility tree and NVDA
- Weekly menu, day cards | each day photo comes before the products and adds a graphic announcement | source and NVDA
- Weekly menu, Friday | photo alt says "Golden butter croissant", but croissants are only baked on Saturday | source review
- Sunday card | the decorative character "休" is exposed with the surrounding text | source and NVDA
- Pre-order and contact forms | name and email inputs have no `autocomplete` attribute | source review
- Pre-order and contact forms | required fields aren't marked in the visible label; the user only finds out on submit | source review
- Pre-order form | a whitespace-only submit sets `#preorder-list.textContent` and wipes the confirmation already shown | source, keyboard and NVDA
- All form fields | `.form-field:focus { outline: none }`. Focus changes the colour of the 1px border | source and keyboard
- Form fields | border #e8ded1 on white is **1.33:1**; on the cream pre-order panel the white field vs cream is **1.22:1** (needs 3:1) | colour calc
- Placeholder text | #a3978c on white is **2.85:1** (needs 4.5:1); labels are present, so the information isn't lost | colour calc
- Filter buttons (unselected) | border #e8ded1 on the white panel is 1.33:1; there is no visible boundary until the hover state | colour calc
- Text colours checked and passing: muted on cream 4.82:1, prices 6.70:1, white on brown 6.70:1, success 6.14:1, error 7.08:1, footer 8.93:1 | colour calc
- Small text | product category 0.65rem (10.4px at the default root size), day count 0.68rem, availability status 11px, mobile hero tagline 10px | source and text-resize check
- Positives seen in source: `lang="en"`, labelled inputs, FAQ uses real buttons with `aria-expanded`/`aria-controls`, filter buttons use `aria-pressed` plus a polite status message, hamburger has `aria-expanded`/`aria-controls`

### Automated tools

- Whole page | **axe-core 4.10.2**: 0 violations, 42 passes, 7 "needs review" (hero text colour contrast, background behind a pseudo-element) | tool: axe
- Whole page, desktop Chrome | **WAVE: 0 errors, 4 contrast errors, 23 alerts** (all "very small text"), **AIM 8.4/10** | [Desktop WAVE summary](screenshots/13-wave-desktop-summary.jpg)
- Whole page, earlier narrower in-app Chromium view | WAVE: 0 errors, 4 contrast errors, 24 alerts (all "very small text"), AIM 8.4/10 | [Earlier WAVE summary](screenshots/01-wave-summary.jpg)
- Hero tagline, h1, description, "Place a Pre-Order" | WAVE compares these four elements against the solid page background without accounting for the photo or gradient. Its contrast view shows **1.44:1** for the tagline against #faf7f1. Hiding the photo confirmed a tagline contrast issue. The overlay over the page background gives the tagline **3.30:1** at the top of the hero | WAVE and colour calculation. [WAVE contrast detail](screenshots/02-wave-hero-contrast.jpg)
- Neither tool flagged the focus, form-border, structure, error-handling or text-resize problems found below
- Whole page | **Lighthouse 13.5.0** (Chrome DevTools, Chromium 157, mobile: Moto G Power, slow 4G, 9:04 AM GMT): **Accessibility 100**, 22 passed, 10 manual checks listed, 41 inapplicable | tool: Lighthouse → [Mobile Lighthouse report](screenshots/12-lighthouse-mobile-100.png)

### Keyboard (in-app browser, Tab / Shift+Tab / Enter / Space only)

- Page load → Tab 1 | lands on the "The Corner Loaf" brand link; there is no skip link, so 6 Tabs are needed to reach the hero buttons. Chrome's default focus ring is clearly visible on the brand and nav links | keyboard
- Tab 7, "Explore Our Menu" | focus ring is a 2px #89502e outline on the darkened photo. It is barely visible; bounded calculation gives 1.0–2.9:1 against the overlay (needs 3:1) | keyboard + colour calc → [Explore Our Menu focus](screenshots/03-focus-explore-menu.png)
- Tab 8, "Place a Pre-Order" | same ring, same problem; the white border looks the same focused and unfocused | keyboard → [Place a Pre-Order focus](screenshots/04-focus-preorder-button.png)
- Tab 9, filter "All Products" | focus clearly visible | keyboard
- Tab, Tab, Enter on "Pastries" | the filter updates the status to "Showing 3 pastry product listings in the weekly menu." Wednesday, Friday and Saturday still show badges of 3, 4 and 3 bakes respectively, with one product on each card | keyboard and desktop Chrome follow-up. [Filtered menu screenshot](screenshots/05-pastries-filter-badge-mismatch.jpg)
- Tab to FAQ 1, Space | expands correctly (`aria-expanded` toggles); the focus ring shows only as a thin line under the question | keyboard → [Expanded FAQ focus](screenshots/07-faq-expanded-focus-clipped.jpg)
- Tab to FAQ 2 (collapsed) | **no visible focus at all**. `document.activeElement` is the button, `:focus-visible` matches, outline is 2px with 4px offset, but `.faq-item { overflow:hidden }` clips it completely. Same on FAQ 3 and 4 | keyboard + DevTools-style JS check → [Collapsed FAQ focus](screenshots/06-faq-focus-invisible.png)
- Tab to pre-order name field | focus is shown only as the 1px border changing colour (`outline:none`); visible but thin | keyboard → [Pre-order field borders](screenshots/08-preorder-field-borders.png)
- Unfocused pre-order textarea | its edge is almost invisible: white box on cream panel, 1.22:1 | keyboard/visual
- Enter on "Send Pre-Order Request", fields empty | the browser's native "fill out this field" message appears and focus moves to the name field. This works | keyboard
- Typed a test order, Enter | the order card and "added successfully" message appear in `#preorder-list` (aria-live polite) | keyboard
- Typed spaces only in both fields, Enter | message "Please complete all required fields before submitting." **replaces the previous order confirmation**. It is in normal body colour (not error red), doesn't say which field, focus stays on the button, and fields get no `aria-invalid` | keyboard → [Whitespace-only pre-order error](screenshots/09-preorder-whitespace-error-wipes-order.jpg)
- No keyboard traps found; Tab order follows the visual order top to bottom | keyboard
- All inputs have programmatic labels (`label[for]`); **none have `autocomplete`** (name ×2, email ×1) | DOM check
- Target size (2.5.8): nav links 19px tall but 28px apart, so they pass on spacing; footer links 24px; inline contact links exempt; filter and FAQ buttons large | JS measurement

### Zoom, text size and reflow (in-app browser viewport emulation)

- 320×720 | no horizontal scroll (scrollWidth 320), nothing clipped. **Reflow passes** | zoom/reflow
- 320px + WCAG text-spacing override (line-height 1.5, letter 0.12em, word 0.16em, paragraph 2em) | no overflow or clipping. **1.4.12 passes** | text spacing
- 640px + page text at 100% | fine
- 640px + root text 150% | fine
- 640px + root text **200%** | the day badge "3 Bakes"/"2 Bak…" is cut off by the card edge: badge right 379px vs card right 309px, `white-space:nowrap` inside `overflow:hidden` | text size → [Day badge at 200% text size](screenshots/10-text-200pct-badge-clipped.jpg)
- 375px phone + root text 200% | the brand name "The Corner Loaf" is `nowrap` and runs past the screen (page scrollWidth 384 > 375, "Loaf" cut off); the hamburger drops to a second row | text size → [Phone header at 200% text size](screenshots/11-phone-375-text-200pct-header.jpg)
- "Scheduled today" badge is fixed `11px` and **does not grow** with text size (11px → 11px at 200%); the hero tagline is fixed 10px on phones | text size

### Structure (Chrome accessibility tree)

- Weekly menu | 7 unnamed `article`s. Products have no list-item structure. Monday's order is `"Bread"` → `heading "Whole Wheat Loaf"` → `"GH₵ 28.00"` → `"Snack"` → `heading "Chin Chin"` → `"GH₵ 20.00"`. The "Snack" category for Chin Chin immediately follows the wheat loaf's price | accessibility tree
- Heading names | With All Products active, the weekly menu has six distinct headings named "Chin Chin", one for each day from Monday through Saturday. A seventh appears in "Today's Scheduled Bakes" on the Saturday tested | count of heading nodes in Chrome's accessibility tree
- Each day | `image "Freshly baked artisan bread"` sits between the day heading and its products; Friday's image is announced as "Golden butter croissant" though croissants are a Saturday bake | a11y tree
- "Today's Scheduled Bakes" | the "Saturday" label is a loose generic after the heading text; the products are h4s inside a `status` live region | a11y tree
- Forms | labels correctly tied to inputs; contact result is a `status` region; pre-order result is `aria-live="polite"` | a11y tree

### Screen reader (NVDA 2026.3.1 + Google Chrome, browse mode, Speech Viewer)

- Page load | before any key press, NVDA read the Today's Scheduled Bakes live region as one run: "Chin Chin GH₵ 20.00 Scheduled todayButter Croissants GH₵ 18.00 Scheduled todayBanana Bread GH₵ 15.00 Scheduled today". There's no heading or context, and the items run together | screen reader
- Hero | line-by-line navigation announces the two lines of the h1 separately: "heading level 1 Freshly Baked," then "heading level 1 Made with Love." | screen reader
- H key through the menu | "Monday heading level 3 / Whole Wheat Loaf heading level 4 / Chin Chin heading level 4 / Tuesday … / Chin Chin …". The sequence includes day headings. Each "Chin Chin" heading has the same name | screen reader
- Down Arrow through Monday | "heading level 3 Monday / Start the week fresh2 Bakes / graphic Freshly baked artisan bread / BREAD / heading level 4 Whole Wheat Loaf / GH₵ 28.00 / SNACK / heading level 4 Chin Chin / GH₵ 20.00 / heading level 3 Tuesday". There's no list or count; the subtitle and badge merge ("fresh2 Bakes"); the category is a loose line after the previous price | screen reader
- Friday | "graphic Golden butter croissant" is read on a day with no croissants | screen reader
- Sunday | "Our day to restClosed休" is merged into one line | screen reader
- FAQ | each question is read twice: "heading level 3 button collapsed How far in advance…" then "heading level 3 button collapsed +". The CSS `::after` "+" is exposed | screen reader
- Forms | "Your Name" is read as text, then "edit required Enter your name". `required` is announced and the labels are read | screen reader
- Filters | "Filter products by category grouping toggle button pressed All Products". Correct roles and states | screen reader
- Pre-order, valid submit (focus mode) | the confirmation was announced as one run: "Test 2 loaves Your pre-order request has been added successfully." | screen reader
- Pre-order, spaces-only submit | NVDA said only "Please complete all required fields before submitting." It didn't name a field, focus stayed on the button, and the loss of the earlier confirmation wasn't announced | screen reader
- Name field | NVDA announced "has auto complete". The DOM inspection showed no declared `autocomplete` token for the field | screen reader and DOM
- Prices | "GH₵ 28.00" is heard as "G H Ghanaian cedis 28…". Understandable, so no issue | screen reader (listened)
