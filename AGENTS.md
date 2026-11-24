## Project and branch targets

The Corner Loaf is a static bakery site deployed on GitHub Pages. Keep it usable as plain HTML, CSS, and browser JavaScript. npm provides shared development tools. See [README.md](README.md) for the local preview and tooling commands.

| Branch           | Start from                   | Pull request target                                                    |
| ---------------- | ---------------------------- | ---------------------------------------------------------------------- |
| `main`           | Permanent production branch  | Keep it deployable.                                                    |
| `develop`        | Permanent integration branch | `main` when releasing                                                  |
| `feature/<name>` | Latest `develop`             | `develop`                                                              |
| `bugfix/<name>`  | Latest `develop`             | `develop` for fixes to unreleased work                                 |
| `hotfix/<name>`  | Latest `main`                | `main` for an urgent production fix, then bring the fix into `develop` |

Use lowercase, hyphen-separated branch names that describe one task, such as `feature/preorder-tracker` or `bugfix/contact-validation`. Release branches are outside the EE03 workflow.

## Branch workflow

1. Switch to `develop` and pull the latest changes before branching. For an urgent production hotfix, start from an updated `main`.
2. Make small, focused commits on the task branch.
3. Before pushing and opening a pull request, incorporate the latest changes from the target branch. Resolve conflicts on your task branch and verify your work again. Rebase an unshared task branch to keep its history clean, or merge the latest target branch into a shared task branch.
4. Push the task branch and open a pull request against the target in the table.

## Commits and history

Use `type(scope): subject` for every new commit you author, including the final squash commit. **Put a specific scope in parentheses immediately after the type.** Write a short, imperative subject. Add a body when the reason for the change needs context, and keep each commit focused on one change.

Types are `feat` for features, `fix` for bug fixes, `docs` for documentation, `style` for formatting-only changes, `refactor` for restructuring that preserves behavior, `test` for tests, `chore` for maintenance, `perf` for performance, and `ci` for continuous integration.

- `feat(preorder): add the order tracker`
- `fix(contact): show errors for required fields`
- `chore(tooling): set up ESLint and Prettier`
- `docs(workflow): document branch and review conventions`

Preserve shared history. Earlier commits predate this file and some use the unscoped `type: subject` format. The starter site was rebuilt in PR #1, EE02 added the accessibility audit and preorder guide, and `main` and `develop` shared the ESLint and Prettier setup commit (`eb7d413`) when this guide was drafted.

## Pull requests and review

- Use a one-line title that summarizes the change. In the description, cover what changed, why it was needed, how it was tested, and any breaking changes. Link the related issue or ticket when there is one.
- Review your own diff first. Run `npm run lint` and `npm run format:check`, and report any existing failures. Add relevant tests and verify changed site behavior in a browser.
- Review for readability, separation of concerns, edge cases, error handling, input safety, hard-coded secrets, and performance where it matters. Check that tests cover key cases and that debug output and local artifacts stay out of the change. Run the branch locally when practical and note how you tested it.
- Label each EE03 review comment `issue`, `suggestion`, `question`, `nitpick`, or `praise`, and mark it `blocking` or `optional`.
- Get at least one approval before merging, or two for substantial changes. Squash and merge task pull requests by default. Use a merge commit when the individual commits need to be preserved. Delete the short-lived branch after it is merged.
