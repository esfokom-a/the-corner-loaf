# Diagnosis of the starter page

I reviewed the HTML, CSS and linked JavaScript, then inspected the local page in Chrome on desktop and at a 390 × 785 phone viewport using responsive emulation. I checked the rendered layout, Chrome's exposed accessibility tree, navigation and a preorder attempt using Tab and Enter.

## Issues and their causes

### 1. The preorder FAQs lack visual hierarchy and clear grouping

The FAQ questions and answers use the same inherited font size and weight, so questions do not stand out as entry points for scanning. The stylesheet defines no rules for `.faq-trigger`, `.faq-body` or `.faq-item`; spacing is left to default paragraph margins. This gives a question a similar gap from its own answer as the answer has from the next question, weakening the principle of proximity: related content is not grouped more closely than separate FAQ pairs.

The root cause is that the HTML groups each question and answer, but the CSS does not translate that relationship into a distinct question style or deliberate spacing within and between groups. Customers checking collection or ordering details have to read through the text to identify where one answer ends and the next question begins, adding effort to a page Marcus wants to be quick and unfussy. ([FAQ markup](index.html#L78), [stylesheet](css/styles.css))

### 2. The menu does not answer “is there bread today?”

The menu presents “This Week's Bakes” and recurring bake days, rather than today's stock. The underlying content describes a production schedule, which cannot tell customers whether a small batch has sold out. A commuter must work out which products match the day and still cannot know whether it is worth stopping. ([HTML](index.html#L25))

### 3. The layout is built for a fixed desktop width

The page has no viewport meta tag, no media queries and several containers fixed at 820px. Padding adds to those widths because the CSS uses the default content-box model: the navigation and main wrapper each occupy 880px. At a 390px phone width in Chrome, the page shrank the desktop layout instead of rearranging it, leaving the four-column menu and FAQ text extremely small. Customers would need to zoom to read the information comfortably. The root cause is a desktop-sized layout with no adaptation to narrow screens, directly conflicting with customers checking mid-walk. ([HTML head](index.html#L3), [CSS](css/styles.css#L11))

### 4. Essential visit information comes too late

The address and hours appear after the full menu, FAQs, preorder form and About section. The page follows a general business-information sequence instead of the customer's immediate visit decision. New visitors have to pass secondary content to find where the bakery is and when they can visit. The short local introduction at the top helps, but the fuller account of Marcus's small-batch bakery is also buried. ([HTML](index.html#L130))

### 5. Navigation labels have no useful destinations

Every navigation link uses `href="#"`; the matching sections have no destination IDs. Clicking Contact in Chrome added a trailing # to the URL and left the page at the top rather than moving to the contact section. The links look like shortcuts but cannot take customers to the menu, location or contact information. Someone trying to avoid scrolling through the clutter gets no useful help from the navigation. ([HTML](index.html#L10))

### 6. Visual structure is not expressed consistently in semantic HTML

The navigation, main content and footer use generic divs, with no `nav`, `main`, `header` or `footer` landmarks. Headings jump from `h1` to `h3`, then later return to `h2`, while Location and Hours are only bold text. The markup encodes appearance more than document structure, making it harder for screen-reader users to navigate directly to the information they need. The root `html` element also lacks `lang="en"`, leaving pronunciation language unspecified. ([HTML](index.html#L2))


### 7. The forms promise actions they cannot complete

Both forms use `type="button"` controls, and the linked script contains comments only. There is no submission handler or configured service to receive an order or message. The preorder form also collects no contact details despite promising that the bakery will get in touch. In Chrome, I entered a test name and order, tabbed to Submit Pre-Order and pressed Enter; the button received focus but produced no confirmation or order entry. Customers could spend time entering a request without it reaching Marcus or providing a way for him to reply. ([Preorder form](index.html#L118), [contact form](index.html#L164), [script](js/script.js))

The fields also rely on placeholders instead of persistent labels, omit `name` attributes, and use a text field for email. Instructions disappear as customers type, and there is no native email-format check. Chrome exposed the fields using their placeholder names, so they were not completely unnamed in this browser; the problem is the lack of persistent labels. These are gaps in the form structure, not just missing decoration.

### 8. Styling rules do not form a consistent system

Text sizes are scattered across inline styles and CSS in both px and pt: the menu and many paragraphs use 12px, while one introduction uses 12pt (16px). Spacing mixes margins, padding, repeated `br` tags and non-breaking spaces. Inline styles override ordinary stylesheet rules for the same properties, making consistent updates harder. Customers encounter different reading sizes and section rhythms without a clear relationship to importance. ([HTML](index.html#L25), [CSS](css/styles.css#L68))




