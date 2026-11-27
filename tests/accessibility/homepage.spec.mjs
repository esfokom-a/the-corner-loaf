import AxeBuilder from "@axe-core/playwright";
import { expect, test } from "@playwright/test";

async function expectNoAccessibilityViolations(page) {
  const { violations } = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();

  const findings = violations.map(({ id, impact, nodes }) => ({
    rule: id,
    impact,
    elements: nodes.map(({ target, failureSummary }) => ({
      target,
      failureSummary,
    })),
  }));
  expect(findings, "axe detected WCAG A or AA violations").toEqual([]);
}

test.beforeEach(async ({ page }) => {
  await page.goto("/");
  await expect(
    page.getByRole("heading", { name: "The Corner Loaf", level: 1 }),
  ).toBeVisible();
});

test("desktop homepage", async ({ page }) => {
  await expect(
    page.getByRole("navigation", { name: "Main navigation" }),
  ).toBeVisible();
  await expectNoAccessibilityViolations(page);
});

test.describe("mobile homepage", () => {
  test.use({ viewport: { width: 390, height: 844 }, hasTouch: true });

  test("with navigation open", async ({ page }) => {
    const navigation = page.getByRole("navigation", {
      name: "Main navigation",
    });
    await expect(navigation).toBeHidden();
    await page.getByRole("link", { name: "Open navigation" }).click();
    await expect(navigation).toBeVisible();
    await expectNoAccessibilityViolations(page);
  });

  test("with a preorder FAQ expanded", async ({ page }) => {
    await page.getByText("How far in advance do I need to order?").click();
    await expect(
      page.getByText("We ask for at least one day's notice"),
    ).toBeVisible();
    await expectNoAccessibilityViolations(page);
  });
});
