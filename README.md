# The Corner Loaf

A mobile-first bakery website built with HTML and CSS. Customers can browse Menu today, check prices and opening hours, and request orders and preorders on WhatsApp. The contact section provides WhatsApp and email links.

[View the live website on GitHub Pages](https://esfokom-a.github.io/the-corner-loaf/).

## Project structure

- `index.html` contains the full page, including today's selection and the usual bake schedule.
- `css/styles.css` holds design tokens and shared styles. The other stylesheets cover the header and footer, bakes, visit information, and preorder and contact sections. Each stylesheet keeps its responsive rules beside the relevant styles.
- `assets/` holds the food photos, favicon and WhatsApp icon.

## Local preview

Open `index.html`, or run `python -m http.server 5500` and visit http://localhost:5500 for a local preview.

## Project notes

Each **Order now** link opens a WhatsApp draft that names the bake and asks about collection. Customers send the message in WhatsApp to request an order.

The **How to order and pick up** guide gives first-time customers three short steps before they open WhatsApp. It explains what to send at least one day ahead, when to wait for confirmation, and where to collect the order. The [EE02 write-up](docs/ee02/write-up.md#further-improvement) explains who it helps and how it was tested.

The preorder and contact forms are deferred until the JavaScript lessons. The [decision log](decisions.md#forms-to-restore-in-the-javascript-lessons) records what to restore.

AI helped with brainstorming, low-level Markdown formatting and wording, and assisted with HTML/CSS implementation, image optimization and checks. I owned the design decisions and final choices, directing and reviewing the work.

See [notes](note.md), [decisions](decisions.md) and [audit](audit.md).
