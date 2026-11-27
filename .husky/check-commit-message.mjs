import { readFileSync } from "node:fs";

const [header] = readFileSync(process.argv[2], "utf8").split(/\r?\n/, 1);
const match =
  /^(feat|fix|docs|style|refactor|test|chore|perf|ci)\(([^()]+)\): (.+)$/.exec(
    header,
  );

if (!match || !match[2].trim() || !match[3].trim()) {
  console.error(
    "Use a commit message in the form type(scope): subject. See CONTRIBUTING.md#commit-messages.",
  );
  console.error("Example: chore(tooling): add Git hooks");
  process.exitCode = 1;
}
