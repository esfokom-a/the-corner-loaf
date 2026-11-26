import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync } from "node:fs";

if (process.env.HUSKY === "0" || !existsSync(".git")) {
  process.exit(0);
}

let hooksPath = "";
try {
  hooksPath = execFileSync("git", ["config", "--get", "core.hooksPath"], {
    encoding: "utf8",
  }).trim();
} catch (error) {
  if (error.status !== 1) throw error;
}

const normalizedPath = hooksPath.replaceAll("\\", "/").replace(/\/$/, "");
if (/(^|\/)AmaliTech\/git-hooks$/i.test(normalizedPath)) {
  // The managed pre-commit hook uses this directory to detect opt-in.
  mkdirSync(".husky/_", { recursive: true });
  console.log(
    "AmaliTech Git hooks are active. The managed pre-commit hook will run ESLint.",
  );
} else if (!hooksPath || normalizedPath === ".husky/_") {
  const { default: install } = await import("husky");
  const message = install();
  if (message) throw new Error(message.trim());
} else {
  console.log(`Existing Git hooks are active at ${hooksPath}.`);
}
