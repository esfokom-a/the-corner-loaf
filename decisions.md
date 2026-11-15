# Decision Log

These decisions explain the final page and how it supports The Corner Loaf's customers.

## Layout and content

- I chose [Sketch A](sketches/corner-loaf-a.png) because it puts opening status, available foods, prices and location before supporting content. This helps commuters decide quickly whether to visit.
- I kept the introduction compact, with a larger bakery name and a double rule for character rather than a large hero section.
- I presented three available foods as a vertical mobile list and three cards on wider screens. Prices use plain bold orange text with consistent currency and decimal formatting.
- I kept the rest of the range in a native "Our other bakes" disclosure, closed by default. It shows original prices and usual bake days, with a clear distinction from today's stock and links to ask about the next availability. This preserves the full range without crowding the initial view.
- I kept descriptions short, with native Read more disclosures for extra detail. The location panel combines the address, directions link and concise weekly hours.
- I kept "Open today" and "Until 5 p.m." with a green indicator as the requested static example. Opening status and availability require manual updates.

## Colours and typography

- I used warm ivory (#FFF8F0) and cream (#FFFCF7) for a welcoming background and cards, dark brown (#38271E) for main text, and muted brown (#6E584B) for supporting text.
- I used burnt orange (#B54708) for prices, links and buttons, pale orange (#FBE8D4) for opening status, and sage (#EDF0E5) for location and hours. These colours separate important information without making the page feel corporate.
- I chose Fraunces 600 from Google Fonts for the bakery name and section headings, with Georgia/serif fallbacks. Arial keeps practical information familiar and readable.

| Text | Mobile | Wider screens |
| --- | --- | --- |
| Bakery name | 40px | 56px |
| Section headings | 24px | 24px |
| Product names | 18px | 20px |
| Prices | 20px | 20px |
| Body text | 16px | 16px |
| Secondary text | 14px | 14px |

## Spacing and responsive CSS

- I used 16px mobile gutters, 20px product-card padding and 24px panel padding. Section gaps increase from 32px to 48px on wider screens to preserve a clear reading rhythm.
- I used a mobile-first layout with one 48rem breakpoint. Grid aligns mobile product content; Flexbox handles navigation, product lists and wider layouts.
- I used simple class selectors and shared variables for spacing, radii, colours and shadows to keep the code consistent and explainable. Spacing names state their pixel size, and the menu width uses the same gutter variable as the page container.

## Navigation and accessibility

- I kept navigation visible in a desktop card. On mobile, an icon-only link opens a vertical, viewport-filling menu using :target; selecting a section or the close icon hides it.
- I used semantic landmarks, a logical heading order, a skip link, visible keyboard focus, labelled fields and descriptive image alternatives. Icon links have accessible names, while decorative icons are hidden from assistive technology.
- I used native details/summary elements for FAQs and product descriptions so they work with taps and keyboards without JavaScript.
- The checked text colours exceed the WCAG AA threshold of 4.5:1, and relevant icons and focus indicators exceed 3:1. The review's results and limitations are recorded in [audit.md](audit.md).

## Food photographs

- I optimized the photographs into WebP using FFmpeg with quality 80 and compression level 6, limiting the larger images to 640px without upscaling.
- I included 176px thumbnail variants with srcset and sizes so mobile browsers can download smaller images. Image dimensions reserve space, while object-fit keeps the photos proportional.

## Contact and forms

- I placed a green WhatsApp icon at the contact card's upper right using absolute positioning, with room reserved beside the heading. Its anchor links to https://wa.me/233551000000, giving customers a direct contact route.
- I kept both forms enabled with labels, required attributes and an email input. Their buttons use type="button"; JavaScript validation, submission and feedback were deferred to the later module. The current buttons do not send orders or messages.
- I kept the page entirely HTML and CSS. The JavaScript exercise file remains unloaded.

## Additional improvement: product availability enquiries

- I added an "Ask about availability" link to each product, opening WhatsApp with its name included in a prepared question. This lets customers check stock before making a trip and gives Marcus clearer enquiries with less back-and-forth.
- I used ordinary wa.me links with encoded message text, accessible product-specific names and a minimum 44px height. Customers review and send the message themselves; opening the link does not confirm availability or place an order. This works without JavaScript.
