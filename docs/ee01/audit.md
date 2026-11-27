# Audit of The Corner Loaf

I reviewed my page against semantic HTML, baseline accessibility and visual consistency, using [W3C WAI Easy Checks](https://www.w3.org/WAI/test-evaluate/easy-checks/), HTML validation and manual Chrome checks. I prioritised the findings by their impact on customers deciding whether to visit the bakery.

This audit covers the earlier version with both forms. The [decision log](decisions.md#forms-to-restore-in-the-javascript-lessons) records their temporary removal.

## Checks and results

- **Semantic HTML:** The W3C HTML checker returned no errors or warnings. The page has clear landmarks, one main heading and a logical heading order. Links navigate to destinations; buttons represent form actions.
- **Accessibility:** Images have descriptive alternatives, fields have connected labels, and icon links have accessible names. Manual keyboard checks covered navigation, product descriptions and FAQs, with visible focus. The checked text colours exceed the WCAG AA threshold of 4.5:1; relevant icons, form boundaries and focus indicators exceed 3:1. These results support a baseline review, not a full WCAG conformance claim.
- **Responsive layout:** The 320px layout was checked in Chrome. Mobile uses a vertical product list and expandable navigation; one mobile-first media query introduces the wider layout. Grid and Flexbox keep related content aligned.
- **Visual consistency:** The warm palette, heading/body font pairing and type hierarchy are consistent. CSS uses simple selectors without inline styles, ID selectors or !important. Repeated spacing, radii, colours and shadows now use shared variables; spacing names indicate their pixel size.

## Chrome Lighthouse results

I ran Lighthouse in Chrome DevTools using an Incognito window and a local HTTP preview. My screenshots record the following results.

| View                                                     | Performance | Accessibility | Best Practices | SEO |
| -------------------------------------------------------- | ----------: | ------------: | -------------: | --: |
| [Desktop screenshot](screenshots/lighthouse-desktop.png) |          98 |           100 |            100 | 100 |
| [Mobile screenshot](screenshots/lighthouse-mobile.png)   |          99 |           100 |            100 | 100 |

Both runs show strong automated results. The screenshots show summary scores rather than individual diagnostic findings. Scores can vary between runs, and an accessibility score of 100 does not replace manual testing.

## Decisions and rationale

| Priority | Decision made                                                                                                                                                                             | Reason for the decision                                                                                                                                      |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1        | I kept the opening status and available foods as manually maintained examples for this HTML/CSS exercise.                                                                                 | This placed the key visit information first while keeping the page static. Its accuracy depends on updating the content when opening hours or stock change.  |
| 2        | I added labelled fields, required attributes and an email input. I kept the forms enabled but deferred JavaScript validation, submission and feedback.                                    | This kept the form structure ready for the next module without introducing JavaScript into the current work. The buttons do not yet send orders or messages. |
| 3        | I placed status, foods, prices and location before supporting content. I used short descriptions, native Read more controls and optimized WebP images with responsive thumbnails.         | These choices helped commuters assess a visit quickly, with less initial reading and smaller image downloads.                                                |
| 4        | I checked selected layouts and keyboard interactions, and recorded the limits of that testing. Full zoom, screen-reader and cross-browser coverage remained outside the completed review. | I reported only what had been checked rather than treating automated scores as proof of complete accessibility.                                              |
| 5        | I consolidated repeated spacing, radii, colours and shadows into shared variables, and derived the menu width from the page gutter.                                                       | This reduced inconsistent values and made later layout changes easier to maintain without adding JavaScript.                                                 |

The validator returned no messages requiring a fix-now, fix-later or ignore decision. My remaining findings concerned static content, deferred form behaviour, testing coverage and visual-system consistency.
