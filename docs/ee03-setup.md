# EE03 setup

## Base-site decision

We chose my version of The Corner Loaf as the shared base for EE03 because the existing commit history was easier to follow and closer to the AmaliTech format we would use for new work. Both repositories used `main` as their base at the time. We started creating `develop` and setting up the development tools after choosing the base. [EE03 team conventions](../CONTRIBUTING.md)

- **Commit history.** Conventional Commits requires a type and a short description and makes the scope optional. My earlier commits already used that format, from `chore: initialize the bakery starter project` to `refactor: split the CSS into shared and section stylesheets`. Ansah Frederick’s early commits included both `docs: add website diagnosis and proposed page structure for The Corner Loaf` and plain descriptions such as `Initial EE01 project setup`. The type prefixes in my history made it easier to scan for features, fixes, and restructuring. For new EE03 commits, we kept that pattern and added the scope required by AmaliTech. [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/#specification) · [My starter commit](https://github.com/esfokom-a/the-corner-loaf/commit/7c17817) · [My CSS refactor](https://github.com/esfokom-a/the-corner-loaf/commit/a788bc1) · [Ansah’s commit history](https://github.com/AnsFredd/the-corner-loaf-redesign/commits/main/)
- **Structure and remaining work.** The selected site has one HTML page, section-specific CSS, a shared stylesheet, and separate assets and lab notes. My EE02 write-up already recorded fixes for the opening-hours example and the skip link. The audit of Ansah’s site recorded form feedback and text clipping issues in the version I tested. On our base, opening hours and availability still need manual updates, and restoring on-site forms is planned for later JavaScript work. We could start the EE03 tooling work using the existing WhatsApp and email flows. [Our EE02 fixes](ee02/write-up.md) · [Peer audit](ee02/audit-of-ansah-frederick.md) · [Form follow-up](ee01/decisions.md#forms-to-restore-in-the-javascript-lessons)

## Local checks and GitHub Actions

- **Shared tooling.** `npm ci` installs the versions in `package-lock.json`. Vite serves the site locally. ESLint checks the browser JavaScript in `js/`, and Prettier checks the site’s HTML, CSS, and JavaScript. [Local setup and commands](../README.md#local-preview)
- **Husky and lint-staged.** The pre-commit hook runs ESLint on staged JavaScript under `js/`. When a file has staged and unstaged edits, lint-staged checks the version going into the commit. The commit-message hook checks the first line for an allowed type, a scope, and a subject. On AmaliTech-managed installations, the managed hook forwards the staged lint check. Automatic message validation depends on it forwarding `commit-msg`. [Husky setup PR](https://github.com/esfokom-a/the-corner-loaf/pull/3) · [Hook setup in the README](../README.md#git-hooks)
- **GitHub Actions.** The CI workflow runs on pushes and PRs targeting `develop` or `main`. Its **ESLint** job runs the full lint and formatting checks on Ubuntu with Node.js 24. We enabled the formatting check after a separate PR cleared the existing Prettier differences. A separate **PR title format** job uses the same subject rule as Husky and runs again when the PR is edited. [CI workflow](../.github/workflows/ci.yml) · [Formatting PR](https://github.com/esfokom-a/the-corner-loaf/pull/5) · [PR title workflow](../.github/workflows/pr-title.yml)
- **Branch rules.** GitHub requires a pull request, one approval, and resolved review conversations on `main` and `develop`. Both branches are protected from deletion and force pushes. The rules for `develop` also require the **ESLint** and **PR title format** checks. [Rules for develop](https://github.com/esfokom-a/the-corner-loaf/rules?ref=refs%2Fheads%2Fdevelop) · [Rules for main](https://github.com/esfokom-a/the-corner-loaf/rules?ref=refs%2Fheads%2Fmain)

## Workflow improvement: automated accessibility checks

I chose to automate accessibility checks because EE02 showed that issues can appear only at a particular viewport size or after a customer opens a control. The checks give us a repeatable way to spot some of those regressions during PR review.

Playwright starts Vite, opens the site in Chromium, and runs axe against three states.

1. The desktop homepage.
2. The mobile homepage with navigation open.
3. The mobile homepage with a preorder FAQ expanded.

The scans cover automatically detectable WCAG 2.1 Level A and AA violations. If axe flags a problem, the **Accessibility** job reports the rule and the affected elements. All three scans passed locally and in GitHub Actions on PR #10. Run them locally with `npm run test:a11y` after installing Playwright’s Chromium browser. [Test suite](../tests/accessibility/homepage.spec.mjs) · [Setup commands](../README.md#accessibility-checks) · [Passing GitHub Actions run](https://github.com/esfokom-a/the-corner-loaf/actions/runs/45983284914/job/140452349678)

Keyboard and screen-reader review still covers interactions such as where focus moves and how content is announced. The PR records a follow-up to scan validation errors and successful submission messages when the on-site forms are restored. [Accessibility PR and follow-up](https://github.com/esfokom-a/the-corner-loaf/pull/10)
