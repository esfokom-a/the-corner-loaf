# EE03 setup

## Base-site decision

We chose my version of The Corner Loaf as the shared base for EE03. It was cheaper for us to bring into the AmaliTech workflow because it already had a history of working on branches and integrating changes through pull requests. The [team conventions](../CONTRIBUTING.md) give us a standard for new work.

- **Commit history.** Ansah Frederick’s early history mixes plain descriptions such as `Initial EE01 project setup` with unscoped subjects such as `feat: build initial bakery website structure using semantic HTML`. My repository also has older unscoped subjects. Rewriting published commits to retrofit scopes would change their IDs and require both contributors to resync. We kept the older history and applied `type(scope): subject` to the commits we authored for EE03. [Ansah’s commit history](https://github.com/AnsFredd/the-corner-loaf-redesign/commits/main/) · [Our integration history](https://github.com/esfokom-a/the-corner-loaf/commits/develop/)
- **Branch history.** Ansah’s repository listed only `main` when I checked it. My site already had a rebuild integrated through a pull request, and we reconciled `main` and `develop` in another pull request. That gave us a production branch to keep deployable and an integration branch for task PRs. Starting from Ansah’s repository would have meant setting up that branch workflow from its single visible branch. [Ansah’s branches](https://github.com/AnsFredd/the-corner-loaf-redesign/branches) · [Site rebuild PR](https://github.com/esfokom-a/the-corner-loaf/pull/1) · [Branch reconciliation PR](https://github.com/esfokom-a/the-corner-loaf/pull/2)
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
