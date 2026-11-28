# EE03 setup

## Base-site decision

We (Elvis Fosu Owusu and Frederick Ansah) chose Elvis’s version of The Corner Loaf as our shared base. Both versions used `main` at the time. Elvis’s existing commit subjects already used prefixes such as `chore` and `refactor`, which made the history easier to scan for setup work and structural changes. Frederick’s early history mixed typed subjects with plain descriptions such as `Initial EE01 project setup`. We chose the base before creating `develop` or adding EE03 tooling. For new work, we kept the typed subjects and added the scope required by AmaliTech. [Starter commit](https://github.com/esfokom-a/the-corner-loaf/commit/7c17817) · [CSS refactor](https://github.com/esfokom-a/the-corner-loaf/commit/a788bc1) · [Frederick’s original repository history](https://github.com/AnsFredd/the-corner-loaf-redesign/commits/main/)

The site already supported the bakery’s main customer tasks. Visitors could browse the menu, check hours and location, and use WhatsApp or email to contact the bakery. The EE02 fixes had also addressed the opening-hours example and skip link. That gave us a working static site on which to practise review and integration. [EE02 write-up](ee02/write-up.md)

## Project structure and conventions

| Path | Purpose |
| --- | --- |
| `index.html` | The single page, including the menu, visit information, preorder guide, About section, and footer. Native HTML and CSS handle navigation and FAQs. |
| `css/` | `styles.css` holds shared colours, type, and spacing. Other stylesheets cover the header and footer, bakes, visit information, and preorder content. Version query strings in `index.html` tell browsers to fetch updated stylesheets after a release. |
| `assets/` and `js/` | Assets include the bakery photos, Marcus’s responsive WebP portrait, and icons. `js/script.js` is a placeholder for later JavaScript work. |
| `docs/` and `tests/accessibility/` | The documentation records project decisions and reviews. The test directory holds the Playwright and axe suite. |

GitHub Pages publishes the repository root from `main`. There is no site compilation step. Vite serves the same static files over HTTP for local preview and automated browser checks. `npm ci` installs the versions recorded in `package-lock.json` so contributors and CI use the same tooling. `package.json` defines the shared commands and development dependencies. `.gitignore` keeps installed packages, generated test results, and local IDE settings out of Git. [Project README](../README.md) · [Package configuration](../package.json) · [Live site](https://esfokom-a.github.io/the-corner-loaf/)

We start routine work from the latest `develop`, use lowercase, hyphenated names such as `feature/responsive-footer`, and open feature and bugfix PRs into `develop`. We release from `develop` into `main`. Authored commits and PR titles use `type(scope): subject`. PR descriptions explain what changed, why it changed, and how it was tested. Reviews label findings by type and state whether each is blocking or optional. The guide calls for one approval, two for substantial changes, and squash merges by default. We used merge commits for the feature pairs below to preserve their individual commits. [Team conventions](../CONTRIBUTING.md) · [Footer release](https://github.com/esfokom-a/the-corner-loaf/pull/15) · [Portrait release](https://github.com/esfokom-a/the-corner-loaf/pull/18)

## Local checks and GitHub Actions

- **ESLint and Prettier.** `eslint.config.mjs` applies the recommended rules to browser JavaScript and recognises names such as `document`, so a typo like `documnt` is flagged before it becomes a runtime error. The empty `.prettierrc` selects Prettier’s defaults. The formatting command covers `index.html`, CSS, and browser JavaScript so diffs stay focused on the change being reviewed. We formatted the existing site before enabling the CI formatting check. [ESLint configuration](../eslint.config.mjs) · [Prettier configuration](../.prettierrc) · [Formatting PR](https://github.com/esfokom-a/the-corner-loaf/pull/5) · [CI formatting PR](https://github.com/esfokom-a/the-corner-loaf/pull/6)
- **Husky and lint-staged.** The npm `prepare` script runs the Husky installer. The `pre-commit` hook calls lint-staged, which runs ESLint on staged files matching `js/**/*.js`. It temporarily hides unstaged edits in partially staged files so a local fix outside the commit cannot mask a lint error. A lint failure blocks the commit. The separate `commit-msg` hook validates the first line. It requires one of `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, or `ci`, followed by a non-blank parenthesised scope, a colon and space, and a non-blank subject. For example, `fix: correct opening hours` fails because it is missing a scope. On AmaliTech-managed installations, the managed hook handles staged linting. Automatic message validation there depends on the managed hooks forwarding `commit-msg`. [Husky setup PR](https://github.com/esfokom-a/the-corner-loaf/pull/3) · [Hook setup in the README](../README.md#git-hooks) · [Message checker](../.husky/check-commit-message.mjs)
- **GitHub Actions.** The CI workflow runs on pushes to any branch and on PRs targeting `develop` or `main`. On Ubuntu with Node.js 24, its **ESLint** job runs `npm ci`, the full JavaScript lint, and the formatting check. It disables Husky because the workflow calls the checks directly. The **Accessibility** job independently runs the browser scans described below. The separate **PR title format** workflow invokes the same validator as the commit hook when a PR to either branch is opened, edited, updated with new commits, or reopened. Rechecking edits catches malformed titles introduced after the initial review. [CI workflow](../.github/workflows/ci.yml) · [PR title workflow](../.github/workflows/pr-title.yml)

### GitHub branch rules

| Branch | Enforced merge requirements | Purpose |
| --- | --- | --- |
| `develop` | Pull request, one approval, resolved review threads, and passing **ESLint** and **PR title format** checks. Branch deletion and force pushes are blocked. | Catch lint, formatting, and naming failures before feature work joins the shared integration branch. [Develop rules](https://github.com/esfokom-a/the-corner-loaf/rules?ref=refs%2Fheads%2Fdevelop) |
| `main` | Pull request, one approval, and resolved review threads. Branch deletion and force pushes are blocked. | Require a reviewed release before updating the branch that GitHub Pages publishes. [Main rules](https://github.com/esfokom-a/the-corner-loaf/rules?ref=refs%2Fheads%2Fmain) |

The **Accessibility** job reports on both PR targets. The required status checks configured on `develop` are the two listed above. [Develop rules](https://github.com/esfokom-a/the-corner-loaf/rules?ref=refs%2Fheads%2Fdevelop)

## Workflow improvements

### Automated accessibility checks

EE02 showed that accessibility problems can depend on screen size or on which control a visitor has opened. We added Playwright and axe so every PR to either shared branch gets the same automated checks, including interactive mobile states. [Accessibility PR](https://github.com/esfokom-a/the-corner-loaf/pull/10)

Playwright uses `playwright.config.mjs` to start Vite at `127.0.0.1:4173` and open Chromium. The suite scans the desktop homepage, the mobile homepage with navigation open, and the mobile homepage with a preorder FAQ expanded. Axe checks automatically detectable WCAG 2.1 Level A and AA violations. Failures identify the rule and affected elements, giving reviewers a place to start. All three scans passed locally and in GitHub Actions on PR #10. The local command is `npm run test:a11y` after installing Playwright’s Chromium browser. [Playwright configuration](../playwright.config.mjs) · [Test suite](../tests/accessibility/homepage.spec.mjs) · [Local setup](../README.md#accessibility-checks) · [Passing Actions run](https://github.com/esfokom-a/the-corner-loaf/actions/runs/45983284914/job/140452349678)

Manual keyboard and screen-reader review still covers focus movement and announcements. We recorded a follow-up to scan error and success states when the on-site forms return. [Accessibility PR follow-up](https://github.com/esfokom-a/the-corner-loaf/pull/10)

### Shared guidance for contributors and AI assistants

We added `CONTRIBUTING.md` as the shared reference for people and linked it from `AGENTS.md` so AI coding assistants working in the repository can follow the same branch, commit, PR, and review conventions. `AGENTS.md` also gives assistants the project constraints, including keeping the site usable as plain HTML, CSS, and browser JavaScript. [Repository instructions](../AGENTS.md) · [Team conventions PR](https://github.com/esfokom-a/the-corner-loaf/pull/8)

## Paired pull requests and conflict resolution

For each feature, we worked on separate branches against `develop`. Once the first PR merged, the other author rebased their feature branch onto the updated `develop`, resolved overlapping edits, and merged the result through a PR. We used the first merge as the baseline and agreed which details from each version belonged in the shared result.

### Responsive footer

Frederick’s PR #14 merged first. It split the footer into brand, navigation, contact, and visit sections. We liked how the address line breaks and horizontal dividers made the narrow layout easier to scan, and how the WhatsApp and email icons made the contact row more compact. Elvis’s PR #13 proposed an orange-and-cream footer and moved the contact actions into it while preserving the existing `#contact` destination. [Frederick’s PR #14](https://github.com/esfokom-a/the-corner-loaf/pull/14) · [Elvis’s PR #13](https://github.com/esfokom-a/the-corner-loaf/pull/13)

Elvis rebased his branch onto `develop` after Frederick’s merge. We resolved the overlapping footer markup and styles by keeping Elvis’s palette and Frederick’s section dividers, address layout, and compact contact row. The merged version uses named WhatsApp and email links with 44 px targets, a single focusable `#contact` destination, and a shorter bakery description. PR #13 records keyboard verification for the contact destination and layout checks from 320 px to 1280 px. Its final lint, formatting, title, and accessibility checks passed. [Combined footer diff](https://github.com/esfokom-a/the-corner-loaf/pull/13/files) · [PR #13 checks](https://github.com/esfokom-a/the-corner-loaf/pull/13/checks)

#### Footer review record

- **PR #14, Elvis to Frederick. Optional suggestion.** Elvis suggested shortening the bakery description to one sentence because the longer copy pushed navigation and contact links farther down on phones. The links still worked, so the change could wait. GitHub shows the thread as resolved, with no written reply from Frederick. The longer copy was still in #14 when it merged. We shortened it to one sentence in the combined footer in #13. [Elvis’s inline comment](https://github.com/esfokom-a/the-corner-loaf/pull/14#discussion_r4721125231) · [Final footer diff](https://github.com/esfokom-a/the-corner-loaf/pull/13/files)
- **PR #14, Elvis to Frederick. Praise.** Elvis approved the PR and praised the address line breaks, horizontal dividers, and compact contact icons because they made the mobile footer easier to scan. The approval called for no change and received no written reply. We kept those details in the combined footer. [Elvis’s approval](https://github.com/esfokom-a/the-corner-loaf/pull/14#pullrequestreview-6090420119)
- **PR #13, Frederick to Elvis. Optional suggestion.** Frederick suggested compact icon links with accessible names because the larger WhatsApp and email controls made the mobile layout feel crowded. Both contact options already worked, so the change was non-blocking. Elvis agreed, replied that he had fixed it, and posted a mobile screenshot. The final diff shows both icons with accessible link names and 44 px targets. Frederick also approved the PR. [Frederick’s comment](https://github.com/esfokom-a/the-corner-loaf/pull/13#issuecomment-7222288951) · [Elvis’s reply and screenshot](https://github.com/esfokom-a/the-corner-loaf/pull/13#issuecomment-7222394264) · [Frederick’s approval](https://github.com/esfokom-a/the-corner-loaf/pull/13#pullrequestreview-6090462362) · [Final footer diff](https://github.com/esfokom-a/the-corner-loaf/pull/13/files)

### Marcus’s portrait in About

Elvis’s PR #16 merged first, with Frederick’s approval. It put a face to the bakery story and kept the existing copy. The portrait stacks below the text on small screens and sits alongside it from `48rem`. A smaller WebP serves phones, and the larger version serves wider screens. Descriptive alt text, explicit image dimensions, and lazy loading help identify the image, reserve its space, and defer its download. [Elvis’s PR #16](https://github.com/esfokom-a/the-corner-loaf/pull/16) · [Portrait markup](https://github.com/esfokom-a/the-corner-loaf/pull/16/files)

Frederick’s PR #17 also proposed a responsive portrait with descriptive alt text, dimensions, and lazy loading. He rebased after PR #16 merged. The overlap was in the same About section, so the rebased result kept one portrait and the layout already integrated by PR #16. The final PR #17 diff contains only formatting changes to older Markdown files because the portrait implementation was already in `develop`. Elvis approved PR #17, and Frederick merged it. [Frederick’s PR #17](https://github.com/esfokom-a/the-corner-loaf/pull/17) · [Final PR #17 diff](https://github.com/esfokom-a/the-corner-loaf/pull/17/files)

#### Portrait review record

Frederick approved Elvis’s PR #16, and Elvis approved Frederick’s PR #17. Both approvals were recorded without written findings. The PRs had no discussion comments, inline threads, or replies, so there were no blocking or optional review requests to address. The portrait shipped through #16, and #17 kept that implementation after the rebase. [Frederick’s approval on #16](https://github.com/esfokom-a/the-corner-loaf/pull/16#pullrequestreview-6092132856) · [Elvis’s approval on #17](https://github.com/esfokom-a/the-corner-loaf/pull/17#pullrequestreview-6093267953) · [Final PR #17 diff](https://github.com/esfokom-a/the-corner-loaf/pull/17/files)

### Follow-up checklist

- [x] Updated PR #17 after reviewing the rebased diff and final checks. Its verification notes now link to the passing formatting check. [Updated PR #17](https://github.com/esfokom-a/the-corner-loaf/pull/17)
- [x] Explained the formatting changes in the merged PR #17. Its description credits PR #16 for the portrait and identifies the three Markdown files as the only changes in #17. For future feature work, put unrelated formatting in a focused PR. [PR #17 description](https://github.com/esfokom-a/the-corner-loaf/pull/17) · [Final diff](https://github.com/esfokom-a/the-corner-loaf/pull/17/files)
- [ ] When on-site forms return, add Playwright and axe coverage for validation errors and successful submissions in the same PR as the forms. Frederick raised this as non-blocking on PR #10, and Elvis agreed and added it to the PR checklist. [Frederick’s suggestion](https://github.com/esfokom-a/the-corner-loaf/pull/10#issuecomment-7216466122) · [Elvis’s reply](https://github.com/esfokom-a/the-corner-loaf/pull/10#issuecomment-7216477420)
