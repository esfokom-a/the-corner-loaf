import { readFileSync } from "node:fs";

const checkingPrTitle = process.argv[2] === "--pr-title";
const header = checkingPrTitle
  ? (process.env.PR_TITLE ?? "")
  : readFileSync(process.argv[2], "utf8").split(/\r?\n/, 1)[0];
const match =
  /^(feat|fix|docs|style|refactor|test|chore|perf|ci)\(([^()\r\n\u2028\u2029]+)\): (.+)$/.exec(
    header,
  );

if (!match || match[0] !== header || !match[2].trim() || !match[3].trim()) {
  const field = checkingPrTitle ? "pull request title" : "commit message";
  const guideSection = checkingPrTitle ? "pull-requests" : "commit-messages";
  console.error(
    `Use a ${field} in the form type(scope): subject. See CONTRIBUTING.md#${guideSection}.`,
  );
  console.error("Example: chore(tooling): add Git hooks");
  process.exitCode = 1;
}
