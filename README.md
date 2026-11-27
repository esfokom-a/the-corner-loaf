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

Install Node.js 24 LTS, then run these commands from the repository root.

```sh
npm ci
npx vite
```

Open the URL Vite prints in the terminal (usually http://localhost:5173).

`npm ci` installs the versions recorded in `package-lock.json`. Without that lockfile-based install, contributors can end up with different tool versions and get different lint or formatting results from the same files.

Vite serves the site over HTTP and updates the preview as you edit. Opening `index.html` directly skips the HTTP requests the deployed site uses to load stylesheets and images, so the local preview would miss problems that only show up when the site is served.

## Linting and formatting

- **ESLint** checks the browser scripts in `js/` when you run `npm run lint`. The config applies ESLint's recommended rules and recognizes browser globals such as `document`. If a script uses `documnt` by mistake, ESLint flags the undefined name. Without the check, the typo can reach the browser and throw a `ReferenceError` only when that code runs.
- **Prettier** gives `index.html` and the files in `css/` and `js/` a consistent format. The empty `.prettierrc` uses Prettier's defaults. Without a shared formatter, contributors' editor settings can produce different indentation and line wrapping, making it harder to spot functional changes in a review. Run `npm run format:check` to detect differences or `npm run format` to apply the formatting. To format a single file, run `npx prettier --write path/to/file`.

Existing site files may report formatting differences. Keep the initial formatting pass and future formatting-only changes in separate commits so reviewers can focus on behavior changes in a pull request. Commit `package-lock.json` when changing tool dependencies so contributors install the same versions.

## Git hooks

Husky sets up the Git hooks during `npm ci`. The `pre-commit` hook runs `npm run lint:staged`, which uses lint-staged to run ESLint on staged JavaScript files in `js/`. When a file has both staged and unstaged edits, lint-staged temporarily hides the unstaged edits so ESLint sees what will be committed. Without that step, an unstaged fix could hide an error in the commit. Run `npm run lint` to check all browser scripts.

The `commit-msg` hook checks that the first line uses an allowed type, a scope, and a subject as described in [AGENTS.md](AGENTS.md). That catches messages like `fix: correct opening hours` before they enter the history.

GitHub Actions runs `npm run lint` and `npm run format:check` on pushes and on pull requests targeting `develop` or `main`.

On machines with AmaliTech-managed Git hooks, the managed `pre-commit` hook runs the repository's lint check. Automatic message validation there requires the managed hooks to forward `commit-msg`. To check a message file manually, run `node .husky/check-commit-message.mjs path/to/message.txt`.

## Project notes

Each **Order now** link opens a WhatsApp draft that names the bake and asks about collection. Customers send the message in WhatsApp to request an order.

The **How to order and pick up** guide gives first-time customers three short steps before they open WhatsApp. It explains what to send at least one day ahead, when to wait for confirmation, and where to collect the order. The [EE02 write-up](docs/ee02/write-up.md#further-improvement) explains who it helps and how it was tested.

The live site handles preorders through WhatsApp and enquiries through WhatsApp or email. The forms in the [initial self-audit](audit.md) were part of an earlier prototype. The [decision log](decisions.md#forms-to-restore-in-the-javascript-lessons) records what to restore during the JavaScript lessons.

AI helped with brainstorming, low-level Markdown formatting and wording, and assisted with HTML/CSS implementation, image optimization and checks. I owned the design decisions and final choices, directing and reviewing the work.

## Documentation

- [Starter-page diagnosis](diagnosis.md), [design notes](note.md), [decision log](decisions.md) and [initial self-audit](audit.md).
- EE02 review of Ansah Frederick’s site. [Audit I wrote](docs/ee02/audit-of-ansah-frederick.md) and [testing log for his site](docs/ee02/testing-log.md).
- EE02 review of this site. [Audit received from Ansah Frederick](https://github.com/AnsFredd/the-corner-loaf-redesign/blob/main/docs/ee02/audit-of-elvis-fosu.md) and [write-up of my fixes and further improvement](docs/ee02/write-up.md).
