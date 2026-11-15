"""Repeatable source checks; complements Lighthouse, not a full HTML/WCAG validator.

Run from the repository root: python audits/check_static.py
Contrast method: https://www.w3.org/TR/WCAG22/#dfn-relative-luminance
"""
from html.parser import HTMLParser
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "css/styles.css").read_text(encoding="utf-8")


class Source(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

    def handle_endtag(self, tag):
        assert self.stack and self.stack.pop() == tag, f"Unbalanced HTML: {tag}"


source = Source()
source.feed(html)
assert not source.stack
elements = source.elements
ids = [a["id"] for _, a in elements if "id" in a]
assert len(ids) == len(set(ids)), "Duplicate IDs"
assert all("style" not in a for _, a in elements), "Inline styles"
for tag, attrs in elements:
    for key in ("aria-labelledby", "aria-describedby", "aria-controls"):
        assert set(attrs.get(key, "").split()) <= set(ids), key
    if attrs.get("href", "").startswith("#"):
        assert attrs["href"][1:] in ids
    if tag == "img":
        assert attrs.get("alt") and attrs.get("width") and attrs.get("height")
        assert (ROOT / attrs["src"]).is_file()
        for candidate in attrs.get("srcset", "").split(","):
            if candidate.strip():
                assert (ROOT / candidate.split()[0]).is_file()
    if tag in {"input", "textarea"}:
        assert any(t == "label" and a.get("for") == attrs.get("id") for t, a in elements)
    if tag == "details":
        assert "open" not in attrs, "Disclosures should start closed"
    assert tag != "script" and not any(k.startswith("on") for k in attrs), "Loaded scripts or event handlers"
assert sum(t == "h1" for t, _ in elements) == 1
for landmark in ("header", "nav", "main", "footer"):
    assert sum(t == landmark for t, _ in elements) == 1
levels = [int(t[1]) for t, _ in elements if re.fullmatch(r"h[1-6]", t)]
assert all(b <= a + 1 for a, b in zip(levels, levels[1:])), "Skipped heading levels"
assert sum(t == "li" and a.get("class") == "product" for t, a in elements) == 3
assert sum(t == "details" for t, _ in elements) == 7
assert all(a.get("type") == "button" for t, a in elements if t == "button")
assert all("disabled" not in a for _, a in elements)
assert "!important" not in css
assert not re.search(r":(?:has|not|is|where|nth-child|first-child|last-child)\b", css)
assert css.count("{") == css.count("}")
assert re.findall(r"@media\s*\(([^)]+)\)", css) == ["min-width: 48rem"]
assert not re.search(r"(?:^|\})\s*#[\w-]+", css), "ID selector"

# Read the actual colour tokens from the stylesheet, not duplicated ratios.
tokens = dict(re.findall(r"--(color-[\w-]+):\s*(#[0-9a-fA-F]{6})", css))


def luminance(color):
    channels = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def passes(fg, bg, minimum):
    dark, light = sorted((luminance(fg), luminance(bg)))
    return (light + 0.05) / (dark + 0.05) >= minimum


contrast = []


def check_pair(label, fg, bg, minimum):
    assert passes(fg, bg, minimum), f"Contrast below threshold: {label}"
    contrast.append({"pair": label, "foreground": fg, "background": bg,
                     "threshold": f"{minimum}:1", "result": "PASS - above threshold"})


for foreground in ("text", "muted", "accent"):
    for background in ("page", "surface", "warm", "sage"):
        check_pair(f"{foreground} on {background}", tokens[f"color-{foreground}"], tokens[f"color-{background}"], 4.5)
check_pair("button text", tokens["color-surface"], tokens["color-accent"], 4.5)
# The muted token is also the form border; accent is the focus outline.
check_pair("form boundary", tokens["color-muted"], tokens["color-surface"], 3)
for selector in ("status-dot-open", "whatsapp-link", "whatsapp-link:hover"):
    rule = re.search(r"\." + re.escape(selector) + r"\s*\{([^}]+)\}", css).group(1)
    background = re.search(r"background:\s*(#[0-9a-fA-F]{6})", rule).group(1)
    if selector == "status-dot-open":
        check_pair("open status indicator", background, tokens["color-warm"], 3)
    else:
        check_pair(selector + " icon", "#ffffff", background, 3)

result = {
    "scope": "Source structure and explicit CSS colour pairs; not full WCAG conformance or HTML validation",
    "source_checks": "PASS",
    "checks": ["balanced HTML tags", "unique IDs and valid fragment/ARIA references",
               "labelled inputs and descriptive image alternatives", "one h1 and ordered headings",
               "header/nav/main/footer landmarks", "three products and seven closed disclosures",
               "enabled forms with non-submitting buttons", "no loaded scripts or inline handlers/styles",
               "one mobile-first media query; no ID selectors, !important or complex pseudo-classes"],
    "contrast_method": "WCAG 2.2 sRGB relative luminance; (Llighter + 0.05) / (Ldarker + 0.05); compare before rounding",
    "contrast_checks": contrast,
}
(ROOT / "audits" / "static-checks.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("PASS: source checks and all listed WCAG contrast thresholds. Evidence: audits/static-checks.json")
