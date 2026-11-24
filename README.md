# The Corner Loaf

A mobile-first bakery website built with HTML and CSS. Customers can browse Menu today, check prices and opening hours, and request orders and preorders on WhatsApp. The contact section provides WhatsApp and email links.

[View the live website on GitHub Pages](https://esfokom-a.github.io/the-corner-loaf/).

## Project structure

- `index.html` contains the full page, including today's selection and the usual bake schedule.
- `css/styles.css` holds design tokens and shared styles. The other stylesheets cover the header and footer, bakes, visit information, and preorder and contact sections. Each stylesheet keeps its responsive rules beside the relevant styles.
- `assets/` holds the food photos, including the 176 px WebP variants used by `srcset`, plus the favicon and WhatsApp icon.
- `js/script.js` is a placeholder for the Applied JavaScript lessons. The current page runs with HTML and CSS and has no script reference.

Fraunces uses Google Fonts’ `display=swap` setting. Headings render in Georgia or the browser’s serif fallback while the web font loads.

## Stylesheet caching

When publishing a CSS change, update the edited stylesheet’s `?v=` value in `index.html` in the same commit. For example, change `css/bakes.css?v=ee02-layout` to `css/bakes.css?v=ee02-layout-2` after editing `css/bakes.css`. If the link has no version value yet, add one. The new URL tells browsers to fetch the updated CSS even if the previous version is cached.

## Local preview

Open `index.html`, or run `python -m http.server 5500` and visit http://localhost:5500 for a local preview.

## Linting and formatting

Install Node.js 24 LTS and run `npm ci` from the repository root to install the shared development tools. The site opens directly in the browser.

- `npm run lint` checks browser JavaScript in `js/` with ESLint's recommended rules.
- `npm run format:check` checks the site's HTML, CSS, and JavaScript against Prettier's defaults.
- `npm run format` applies Prettier formatting to those files. To format a single file, run `npx prettier --write path/to/file`.

Existing site files may report formatting differences. Keep the initial formatting pass and future formatting-only changes in separate commits so reviewers can focus on behavior changes in a pull request. Commit `package-lock.json` when changing tool dependencies so contributors install the same versions.

## Project notes

Each **Order now** link opens a WhatsApp draft that names the bake and asks about collection. Customers send the message in WhatsApp to request an order.

The **How to order and pick up** guide gives first-time customers three short steps before they open WhatsApp. It explains what to send at least one day ahead, when to wait for confirmation, and where to collect the order. The [EE02 write-up](docs/ee02/write-up.md#further-improvement) explains who it helps and how it was tested.

The live site handles preorders through WhatsApp and enquiries through WhatsApp or email. The forms in the [initial self-audit](audit.md) were part of an earlier prototype. The [decision log](decisions.md#forms-to-restore-in-the-javascript-lessons) records what to restore during the JavaScript lessons.

AI helped with brainstorming, low-level Markdown formatting and wording, and assisted with HTML/CSS implementation, image optimization and checks. I owned the design decisions and final choices, directing and reviewing the work.

## Documentation

- [Starter-page diagnosis](diagnosis.md), [design notes](note.md), [decision log](decisions.md) and [initial self-audit](audit.md).
- EE02 review of Ansah Frederick’s site. [Audit I wrote](docs/ee02/audit-of-ansah-frederick.md) and [testing log for his site](docs/ee02/testing-log.md).
- EE02 review of this site. [Audit received from Ansah Frederick](https://github.com/AnsFredd/the-corner-loaf-redesign/blob/main/docs/ee02/audit-of-elvis-fosu.md) and [write-up of my fixes and further improvement](docs/ee02/write-up.md).
