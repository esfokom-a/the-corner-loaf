import { defineConfig } from "@playwright/test";

const baseURL = "http://127.0.0.1:4173";

export default defineConfig({
  testDir: "./tests/accessibility",
  workers: 1,
  use: {
    baseURL,
    browserName: "chromium",
    viewport: { width: 1280, height: 800 },
  },
  webServer: {
    command: "npm exec -- vite --host 127.0.0.1 --port 4173 --strictPort",
    url: baseURL,
  },
});
