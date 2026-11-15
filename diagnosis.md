# Diagnosis of the starter page

I reviewed the HTML, CSS and linked JavaScript, then inspected the local page in Chrome on desktop and at a 390 x 785 phone viewport using responsive emulation. I checked the rendered layout, Chrome's exposed accessibility tree, navigation and a preorder attempt using Tab and Enter.

## Ranked issues and their causes

I ranked these findings by how directly they prevent customers from deciding whether to stop in, how widely they affect access to the information, and whether they block a customer action. The brief says customers check their phones “mid-walk” and may “give up scrolling and just keep walking”. That makes today's stock, phone readability and visit details the first priorities. A lower rank does not make an issue optional; forms, for example, completely fail for customers who try to use them.

### 1. The menu does not answer “is there bread today?”

The menu presents “This Week's Bakes” and recurring bake days rather than today's stock. The root cause is a content model based on the production schedule, which cannot tell customers whether a small batch has sold out. A commuter must match products to the day and still cannot know whether it is worth stopping. I ranked this first because it leaves Marcus's exact question unanswered: “whether there is bread today.” ([HTML](index.html#L25))

### 2. The fixed desktop layout makes the page difficult to read on a phone

The page has no viewport meta tag, no media queries and several containers fixed at 820px. Default content-box sizing adds padding to those widths, making the navigation and wrapper 880px wide. At a 390px phone width in Chrome, the page shrank the desktop layout instead of rearranging it, leaving menu and FAQ text extremely small. The root cause is a desktop-sized layout with no adaptation to narrow screens. Customers checking mid-walk must zoom and navigate the enlarged page just to read the shelf, increasing the effort that the brief says makes them walk on. ([HTML head](index.html#L3), [CSS](css/styles.css#L11))

### 3. Essential visit information comes too late

The address and hours appear after the full menu, FAQs, preorder form and About section. The root cause is a general business-information sequence rather than an order built around the immediate visit decision. A new customer can find a product they want but must continue past unrelated content to establish where the bakery is and whether they can visit. I ranked this above secondary interactions because Marcus is trying to retain quick morning walk-by traffic. ([HTML](index.html#L130))

### 4. Missing semantic structure makes essential information harder to navigate

The navigation, main content and footer use generic divs without `nav`, `main`, `header` or `footer` landmarks. Headings jump from `h1` to `h3`, then return to `h2`; Location and Hours are only bold text. The root cause is markup chosen for appearance rather than document meaning. Customers using screen-reader landmark or heading navigation have fewer useful routes to the shelf and visit details, making the same quick stop-in decision more laborious. The missing `lang="en"` also leaves pronunciation language unspecified. This affects access to the whole page, so it takes priority over individual supporting sections. ([HTML](index.html#L2))

### 5. Navigation offers shortcuts that do not work

Every navigation link uses `href="#"`, and the corresponding sections have no destination IDs. Clicking Contact in Chrome added a trailing # and left the page at the top. The root cause is placeholder destinations that were never connected to the content. Customers trying to bypass the long page get no help from its shortcuts and must resume scrolling, reinforcing the frustration described in the brief. ([HTML](index.html#L10))

### 6. Forms consume customers' time without completing their requests

Both forms use `type="button"`, while the linked script contains comments only: there is no submission handler or configured receiving service. In Chrome, I entered a test name and order, tabbed to Submit Pre-Order and pressed Enter; the button received focus but produced no confirmation or order entry. The preorder form also collects no contact details despite promising a reply. The root cause is an interface presented without the processing or information needed to fulfil it. Customers can spend time requesting bread without Marcus receiving the request, undermining confidence in a small, personal business. I ranked this below the immediate visit barriers because preordering is a secondary journey, although it is a complete failure within that journey. ([Preorder form](index.html#L118), [contact form](index.html#L164), [script](js/script.js))

Fields also rely on placeholders rather than persistent labels, omit `name` attributes and use a text field for email. Instructions disappear during entry and there is no native email-format check, making requests harder to complete correctly on a phone. Chrome exposed placeholder-derived names, so the fields were not completely unnamed in this browser.

### 7. The preorder FAQs lack visual hierarchy and proximity

Questions and answers inherit the same font size and weight. There are no CSS rules for `.faq-trigger`, `.faq-body` or `.faq-item`, leaving spacing to default paragraph margins. A question has a similar gap from its answer as that answer has from the next question. The root cause is that the HTML groups each pair but the CSS does not express that relationship through emphasis and closer spacing within groups. Customers checking collection or cancellation details must read through the text to identify each pair, adding work to an experience Marcus wants to feel unfussy. I ranked this below the failed actions because the answers remain visible and readable at desktop size, despite being harder to scan. ([FAQ markup](index.html#L78), [stylesheet](css/styles.css))

### 8. Inconsistent styling weakens reading order and the shop's identity

Font sizes are scattered across inline styles and CSS: the menu and many paragraphs use 12px, while one introduction uses 12pt (16px). Spacing mixes margins, padding, repeated `br` tags and non-breaking spaces. The root cause is a collection of individual formatting choices rather than a shared type and spacing system; inline styles also override ordinary stylesheet rules for the same properties. Customers encounter changing text sizes and gaps without a clear relationship to importance. This makes scanning less predictable and works against the brief's warm, unfussy impression. I ranked the remaining visual inconsistency last because the more immediate reading and navigation barriers above directly obstruct the visit decision. ([HTML](index.html#L25), [CSS](css/styles.css#L68))
