# EE02 write-up: fixes and further improvement

- My site: [The Corner Loaf on GitHub Pages](https://esfokom-a.github.io/the-corner-loaf/)
- Audit received from: Ansah Frederick, [accessibility audit of my site](https://github.com/AnsFredd/the-corner-loaf-redesign/blob/main/docs/ee02/audit-of-elvis-fosu.md)

## Fixes

Ansah Frederick found no confirmed WCAG 2.2 Level AA violations in the checks of my site. I numbered his two observations in the order they appear in the audit I received.

### Finding 2: The focused skip link overlaps the page title

- **Reproduced before fixing:** Yes. At 200% zoom in Chrome, the focused skip link overlapped the top of the title. It cleared the title at 100% in the desktop window tested. Enter still reached the main content.
- **Cause:** The original absolute positioning placed the focused link over the header without reserving space for it.
- **What I changed:** In `css/styles.css`, the link stays visually hidden until focused. On focus it takes up its own space above the header and shows the existing focus outline. [Skip-link styles at the EE02 submission commit](https://github.com/esfokom-a/the-corner-loaf/blob/d3a8e7370921c5d94451bd3a761754ef77d9cb84/css/styles.css#L99-L117)
- **Why this fixes the cause, not just the symptom:** The focused link participates in the normal page layout. The header follows the link even when the width or zoom changes.
- **How I verified it:** In Chrome, the first Tab showed the link above the title at 100% and 200% desktop zoom and at 393 CSS px in mobile emulation. Enter reached the main content at 200% and in the mobile preview.

## Issues I found myself

- The “Menu today” list is maintained manually and can still show a bake after it sells out. I added a note and a link to the contact section so customers can check before visiting. In Chrome’s 393 CSS px preview, the note wrapped and I reached “Get in touch” using Tab and Enter. [My original audit](../../audit.md#decisions-and-rationale) · [Menu note](../../index.html#L67)

## Findings I did not fix, or disagree with

- **Finding 1: Opening-hours wording.** I kept “Open today” and “Until 5 p.m.” near the top of the page. Customers passing the bakery can glance at their phone to see whether the shop is open and when it closes. The opening-hours link gives them the full schedule if they want to plan a visit. The status is maintained manually. It needs to reflect the current day, since the weekly schedule lists a 2 p.m. closing time on Saturday and shows Sunday as closed. [Opening panel](../../index.html#L54) · [Weekly schedule](../../index.html#L161)
- **WAVE’s six possible-heading alerts on menu prices.** My Chrome WAVE check on the live site reproduced six alerts, zero errors, zero contrast errors, and an AIM score of 9.9/10. I confirmed that the six prices use paragraphs and the product names use headings. The prices keep their paragraph markup. [Peer review of the alerts](https://github.com/AnsFredd/the-corner-loaf-redesign/blob/main/docs/ee02/audit-of-elvis-fosu.md#wave-possible-heading-alerts--reviewed-not-a-heading-failure)

## Further improvement

- **Who it helps:** Customers who benefit from plain language and a predictable sequence, like Sophie in the W3C user story. It also helps first-time customers ordering on a phone. [Sophie’s story](https://www.w3.org/WAI/people-use-web/user-stories/story-five/)
- **The barrier they faced:** The preorder panel told customers what to send. They had to look through separate FAQs to learn how far ahead to order and how pickup works. Someone following the WhatsApp link could leave the page without knowing to wait for a reply before visiting.
- **What I built:** I put a numbered guide above the WhatsApp link. It tells customers to send their name, order and pickup day at least one day ahead, wait for Marcus to confirm a time, and collect at 17 Boundary Road, East Legon. The WhatsApp link carries a draft with matching prompts. [Preorder guide](https://esfokom-a.github.io/the-corner-loaf/#preorder)
- **Why it is worth doing for the business:** Clear instructions at the point of ordering can reduce incomplete requests and follow-up messages. Marcus can keep using the same WhatsApp process, with only a short guide to maintain.
- **How I tested it:** I walked through a first-time Saturday pickup in Chrome’s 393 CSS px mobile preview. From the mobile menu, I could find when to message, what to send, and where to go after confirmation using the guide alone. All three steps and the button fit at that width and at 200% desktop zoom. Chrome’s accessibility tree exposed three list items before the named WhatsApp link. Tab reached the link with a visible outline, and the draft URL contained prompts for name, order and pickup day. I also confirmed that the link opened WhatsApp successfully.
