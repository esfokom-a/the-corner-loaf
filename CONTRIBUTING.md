# Contributing to The Corner Loaf

Follow these AmaliTech EE03 team conventions for branches, commits, pull requests, and reviews. See the [README](README.md) for local setup and tooling.

## Branches

| Branch                   | Purpose                                                | Merge into           |
| ------------------------ | ------------------------------------------------------ | -------------------- |
| `main`                   | Stable, production-ready code. Keep it deployable.     |                      |
| `develop`                | Integrate finished development work here first.        | `main` at release    |
| `feature/<feature-name>` | Add a feature or enhancement.                          | `develop`            |
| `bugfix/<issue-name>`    | Fix an issue in work that has yet to reach production. | `develop`            |
| `hotfix/<issue-name>`    | Fix an urgent production issue.                        | `main` and `develop` |

Use lowercase, hyphen-separated names such as `feature/preorder-tracker` and `bugfix/contact-validation`. Keep one task per branch. Routine EE03 work uses `main`, `develop`, and feature or bugfix branches. Release branches are outside EE03.

1. Switch to `develop` and pull the latest changes. For an urgent production hotfix, start from the latest `main`.
2. Create a branch named for the task and make small, focused commits as you work.
3. Before pushing, pull the latest changes from the target branch into your task branch, resolve conflicts there, and verify the result. Rebase an unshared feature branch to keep its history clean. Use a merge when integrating a feature or hotfix branch where the individual commits need to be preserved.
4. Push the task branch and open a pull request against the target above.

## Commit messages

Use `type(scope): subject` for each commit you author, including the final squash commit. The scope is required and identifies the part of the project affected. Use a short subject that describes the change. Each commit should do one thing.

| Type       | Use it for                                   |
| ---------- | -------------------------------------------- |
| `feat`     | A new feature                                |
| `fix`      | A bug fix                                    |
| `docs`     | Documentation                                |
| `style`    | Formatting without behavior changes          |
| `refactor` | Restructuring code without changing behavior |
| `test`     | Adding or changing tests                     |
| `chore`    | Maintenance, such as dependency updates      |
| `perf`     | Performance improvements                     |
| `ci`       | Continuous integration changes               |

Examples include `feat(preorder): add the order tracker`, `fix(contact): validate the email field`, and `chore(deps): update Node packages`.

If the subject needs more context, leave a blank line and add a body. It can span several lines or paragraphs. Explain what changed and why it matters. For a breaking change, add a `BREAKING CHANGE:` footer after a blank line and explain what affected users or contributors need to do. Also call it out in the pull request description. See [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

```text
fix(contact): preserve enquiry details after validation

Keep the customer's message in the form so they can correct their email
address without retyping the enquiry.
```

## Pull requests

Use a one-line title in the same `type(scope): subject` format as [commit messages](#commit-messages), such as `fix(contact): preserve enquiry details after validation`. GitHub Actions checks the title on pull requests targeting `develop` or `main` and reruns the check after edits.

In the description, explain what changed, why it was needed, how it was tested, and whether it introduces breaking changes. Link the related issue or ticket when one exists.

Review your own diff before requesting review. Run `npm run lint` and `npm run format:check`, add tests where they apply, and verify changed site behavior in a browser.

## Reviews and merging

Check structure, separation of concerns, clear names, small functions, and unnecessary repetition or complexity. Look at edge cases and error handling. Verify that user input is handled safely, secrets stay out of the code, and performance is appropriate. Check that tests cover important cases and that the diff contains no debug logs or unrelated local files.

When practical, pull the branch and run it, then say on the pull request how you tested it. Label each EE03 review comment `issue`, `suggestion`, `question`, `nitpick`, or `praise`, and mark it `blocking` or `optional`.

Get at least one reviewer approval before merging and two for substantial changes. Squash and merge by default. Use a merge commit when the individual commits need to be preserved. Delete the task branch after it merges. For an urgent hotfix, also integrate the fix into `develop`.
