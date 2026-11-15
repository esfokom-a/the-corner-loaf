# Decision Log

Each entry records what we chose and why it helps The Corner Loaf or its customers.

## Layout and sketch

- I chose a mobile-first, single-column hierarchy, because commuters checking mid-walk need to recognise the bakery, see today's availability and find its location quickly.
- I chose Sketch A (`sketches/corner-loaf-a.png`) because it puts opening status and the product list before supporting content, helping commuters see what they can buy sooner than Sketch B's large image and preorder-led introduction.

## Design system

### Colour palette

- I chose warm ivory (#FFF8F0) for the page background and light cream (#FFFCF7) for cards, forms and FAQ panels because their near-white warmth reflects Marcus's welcoming, unfussy shop while keeping the content clear.
- I chose burnt orange (#B54708) for primary buttons, links and selected controls because a restrained warm accent suits the bakery and helps commuters recognise where they can act; the checked button-text and link/background combinations exceed the WCAG AA normal-text threshold of 4.5:1.
- I chose dark brown (#38271E) for headings, body text and product names, and muted brown (#6E584B) for supporting descriptions because customers checking mid-walk need readable information with a clear order of importance; both exceed the WCAG AA normal-text contrast threshold of 4.5:1 against warm ivory. Prices use the orange accent.
- I chose pale orange (#FBE8D4) for today's availability or opening-status panel and pale sage (#EDF0E5) for location and hours because grouping these visit essentials helps customers decide whether to stop; the checked brown-text combinations exceed the WCAG AA normal-text contrast threshold of 4.5:1 on both surfaces.

### Typography

- I chose Fraunces from Google Fonts at weight 600 for the bakery name and section headings, with Georgia and serif fallbacks, because its expressive, warm character gives Marcus's small bakery a personal identity; the fallbacks keep headings readable while the font loads.
- I chose Arial with sans-serif fallbacks for product names, descriptions, prices, hours, FAQs and forms because familiar, straightforward letterforms help customers scan practical information quickly without requiring another font download.
- I chose a mobile type scale of 40px for the bakery name, 24px for section headings, 18px bold for mobile product names and FAQ questions, 20px for prices, 16px for body text and hours, and 14px for secondary details. The larger name and a short double rule echo Sketch A and give the header a distinctive identity without introducing a hero section.
- I increased the bakery name to 56px and product names to 20px on wider screens, where they have room to stand out.
- I chose line heights of 1.5 for body text, 1.65 for product descriptions, 1.2 for main/section headings and 1.35 for product names because descriptions and answers need breathing room, while compact headings keep the first part of the page focused on the three vital answers.

### Spacing

- I used a shared spacing scale for forms and FAQs and repeated 8, 16, 24, 32 and 48px steps elsewhere. Product cards also use 20px padding and gaps. Some repeated values remain literal CSS values rather than custom properties; the system is not completely tokenized. The audit records this as a maintenance issue.
- Mobile page gutters are 16px, product-card padding is 20px, and visit/form panel padding is 24px. Main section gaps are 32px on phones and 48px from the 48rem breakpoint. Product tiles have 16px gaps; FAQ cards have 24px gaps and 16px padding.

## Semantic structure and accessibility

- I chose semantic header, navigation, main, section, address and footer elements, one h1 and ordered section headings because customers using assistive navigation need direct routes to the same shelf and visit information as everyone else.
- I chose a skip link, visible focus outlines, underlined text links and primary standalone controls at least 44px high because keyboard users and customers tapping a phone mid-walk need clear, easy-to-reach navigation without relying on colour alone; WCAG 2.2 Level AA is the accessibility target, rather than an unverified conformance claim.
- I chose persistent form labels, appropriate input types and autocomplete attributes because customers should retain the context of each field while entering their details. Both forms remain enabled as part of the static interface; their current implementation limits are documented below.

## HTML-only interactions and content

- I kept native details and summary disclosures for FAQs, where built-in keyboard operation and expanded-state announcements work without JavaScript.
- I replaced the navigation disclosure with a permanent horizontal navigation card from 48rem upwards. There is no desktop menu toggle.
- On smaller screens, an icon-only hamburger link opens a vertical navigation area that fills at least the viewport. The close icon appears at its upper right. The simple `.site-menu:target` rule shows the navigation when the URL ends in `#navigation`; choosing a section or Close changes the fragment and hides it. These are ordinary links with accessible names, rather than buttons with an inaccurate static expanded state.
- I kept the mobile navigation in normal document flow. Opening it scrolls it into view and pushes subsequent content below it. This avoids covering focusable background content or requiring a JavaScript modal focus trap. Navigation and section destinations have `tabindex="-1"` so fragment navigation can move keyboard focus to them. Closing returns to the top of the page. Browser Back may reopen a previous fragment, as with standard anchor navigation.
- I replaced the six-item carousel with a short static "Available today" selection: Sourdough Loaf, Whole Wheat Loaf and Chin Chin. These three items are the example shelf, rather than the complete catalogue. On mobile, compact rows stack vertically with the image, description and price together; wider screens show three cards side by side. There is no sideways scrolling or extra carousel keyboard stop.
- I kept the concise three-row weekly hours list: Monday-Friday 7am-5pm, Saturday 7am-2pm, Sunday closed. The example shelf no longer shows recurring bake-day labels, because this section describes what is available today.
- At the user's request, the static demonstration says "Open today" and "Until 5 p.m.", with a green indicator. This example is independent of the actual calendar date. Opening status and the three available products are manually authored demonstration content; no JavaScript, live stock feed or time calculation is used.
- I simplified the location panel to “Visit the bakery”, the full address, a restrained “Get directions” link with a decorative map-pin icon, and the grouped hours.
- I kept the existing prices, opening hours, address and contact details, and rewrote the product descriptions for shorter previews with optional detail. The three available foods now use the supplied photographs, replacing the temporary image placeholders.

## Responsive implementation

- I chose CSS custom properties for colour, fonts, type sizes, line heights, spacing and shared component dimensions because one consistent system keeps Marcus's page coherent and makes future changes easier to maintain.
- I used a single 48rem breakpoint for the desktop navigation card, larger bakery name, three-card product layout, and side-by-side address and hours. Sketch A's reading order remains intact.
- I used Flexbox for the header, navigation, product list and location panel, and border-box sizing to keep the layout responsive. Selectors use explicit classes, simple descendants, and basic states such as `:target`, `:hover`, `:focus-visible`; there are no `:has()`, `:not()` or positional pseudo-classes.
- I kept the name beside the hamburger on phones, allowing the title to wrap at narrow widths rather than shrinking the text or overflowing.
- I removed the script reference from the HTML. The existing JavaScript exercise file remains untouched and does not load on this static page.
- I kept visible keyboard focus, a skip link, labelled navigation and product sections, semantic headings, 48px menu controls, and persistent form labels. Decorative SVG icons and the status dot are hidden from assistive technology; their meanings are supplied by link names or adjacent text. Accessibility remains a WCAG 2.2 AA target, not a claim of a completed conformance audit.
- I loaded only Fraunces 600 with font-display swap and kept Arial for practical text because the bakery needs its warm heading character without delaying readable prices, hours and descriptions while fonts load.

## WhatsApp shortcut

- I added a green WhatsApp chat-and-phone SVG icon as an ordinary anchor to `https://wa.me/233551000000`, using the existing Ghana number in international format. The contact text says "Chat on WhatsApp" instead of displaying the number or raw URL.
- I used simple absolute positioning within the relatively positioned contact card. The icon sits at the upper right, with space reserved beside the heading so it does not cover text or follow the visitor over other content.
- The icon link has the accessible name "Chat with The Corner Loaf on WhatsApp", a 52px tap target and the shared visible keyboard focus outline. Its decorative SVG is hidden from assistive technology. White on the darker green background provides more than 3:1 contrast for the graphic. The link uses normal browser navigation, which can hand off to WhatsApp; no script or automatic message sending is involved.

## Optimized food photographs

- I made all three food images used by the page WebP. I used the locally installed FFmpeg with libwebp, quality 80 and compression level 6, removed metadata, and limited image width to 640px without upscaling. The two JPEGs were converted; the existing Chin Chin WebP was optimized further. The unused source originals were removed; the page references only the optimized food assets.
- The larger WebP sources are `assets/sourdough-loaf.webp`, `assets/whole-wheat-loaf.webp` and `assets/chin-chin.webp`. Each also has a 176px `-small.webp` version. Native `srcset` and `sizes` let the browser choose an appropriate download for the 88px mobile thumbnail or larger desktop card. All six image files are referenced by the HTML.
- I used actual img elements with descriptive alt text and intrinsic width and height attributes. Simple object-fit styling keeps square mobile thumbnails and larger desktop photographs consistent without stretching them. This preserves the vertical mobile food list and requires no JavaScript.

## Available-today tile refinement

- I modernized the three food tiles with a consistent rounded surface, a subtle shadow, larger photographs and aligned spacing. On phones, a simple two-column Grid places the photo beside the name and price, then lets the description span the full card width. This removes the narrow description column caused by keeping image, text and price in three competing columns. The tiles remain a vertical list; desktop retains three equal-width cards.
- I display each price as plain bold orange text beneath the product name, with a consistent currency symbol and two decimal places. At the user's request, I removed the badge background, border, padding and unit labels, along with the extra pricing wrapper and currency/amount spans. Prices remain GH cedi 35.00, 28.00 and 20.00, using tabular numerals for consistent alignment.
- I expanded the descriptions with texture, serving suggestions and portion context based on the existing product information. A light divider separates the readable, full-width description from the product identity and price. No new ingredients, dietary claims or stock guarantees were added.
- I kept the same high-contrast brown and orange palette, real image alt text, native list semantics, simple class selectors and HTML/CSS-only implementation.

## Short descriptions with optional detail

- I reduced each food tile's initial description to one short sentence. The fuller texture, serving and portion details sit in a native HTML details element, closed by default, with a "Read more" summary.
- Tapping or clicking the summary opens and closes the extra text. The browser supplies keyboard operation and announces the expanded or collapsed state without JavaScript. Each summary has an accessible name identifying its product, retains the native disclosure marker and shared focus outline, and has a minimum height of 44px.
- I used simple class selectors for spacing and kept all descriptive content in the HTML, so the page remains static and easy to explain.

## Enabled preorder and contact forms

- At the user's request, I enabled both form fieldsets and removed all "coming soon" button and legend text and all on-page "isn't available yet" messages. The buttons read "Submit preorder" and "Send message"; the fieldsets have concise legends and retain their persistent labels and input attributes.
- These are static interface examples for now. The existing JavaScript file contains exercise comments only; there is no submission handler, preorder tracker, message processing or receiving service. Clicking either button does not place an order, send a message or display a success confirmation. Implementation will follow in the JavaScript work.
- I used enabled `type="button"` controls until submission is implemented, so clicking them does not trigger the browser's default GET submission, reload the page or put entered details in the URL. No JavaScript was added or loaded. The WhatsApp and email links remain available as contact routes.

## Verification and cleanup

- I checked the implementation against this log and corrected outdated claims about price colour, spacing, image files and type sizes. I record contrast as exceeding the applicable WCAG threshold, rather than giving exact calculated ratios.
- The current findings, validator result, Lighthouse results and limits of the review are in [audit.md](audit.md). This is a first review, not a full WCAG conformance claim.
- I retained the referenced food photographs, responsive thumbnail variants and favicon. I removed the unused local font download and its accompanying licence; the Google Fonts stylesheet remains the active font source. Sketches and the unloaded JavaScript exercise file remain part of the coursework.
- At the user's request, detailed audit reports and the temporary check script were removed with the audits folder. The written audit is the retained diagnosis.
