"""Mechanical checks of plugin content (validation gate items that a script can verify).

Usage: python scripts/check_content.py   -> exit 1 on any failure.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = [
    "sockets-chipsets", "memory", "power-supplies-connectors", "form-factors-cases", "gpu-bandwidth-ai",
    "retailers-by-country", "retailer-criteria", "international-buying", "research-method", "used-market-checklist",
]
SKILLS = ["build-config", "check-compatibility", "hunt-prices", "size-local-ai", "review-used-listing", "track-price"]
BANNED = re.compile(r"(?i:open[- ]source)|\bMIT\b")
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    return dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line and not line.startswith(" "))


def check_reference(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    name = path.relative_to(ROOT).as_posix()
    if "Last checked: 2026-" not in text[:600]:
        fail(f"{name}: missing 'Last checked' line near the top")
    if not re.search(r"^## Not verified", text, re.M):
        fail(f"{name}: missing '## Not verified'")
    m = re.search(r"^## Sources.*$", text, re.M)
    if not m:
        fail(f"{name}: missing '## Sources'")
        return
    body, sources = text[: m.start()], text[m.end():]
    listed = set(re.findall(r"^\s*(?:[-*]\s*)?\[?(\d+)[\].]", sources, re.M))
    cited = set(re.findall(r"\[(\d+)\]", body))
    missing = sorted(cited - listed, key=int)
    if missing:
        fail(f"{name}: cited but not in Sources: {missing[:10]}")
    if not cited:
        fail(f"{name}: no [n] citations")


def check_skill(skill: str) -> None:
    path = ROOT / "skills" / skill / "SKILL.md"
    if not path.exists():
        fail(f"{skill}: SKILL.md missing")
        return
    text = path.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if set(fm) != {"name", "description"}:
        fail(f"{skill}: frontmatter must be exactly name+description, got {sorted(fm)}")
    desc = fm.get("description", "")
    if fm.get("name", "").strip() != skill:
        fail(f"{skill}: name mismatch")
    if not desc.strip().startswith("This skill should be used"):
        fail(f"{skill}: description not in third person ('This skill should be used...')")
    if len(desc) > 1024:
        fail(f"{skill}: description {len(desc)} chars > 1024")
    if len(re.findall(r'"[^"]{6,}"', desc)) < 5:
        fail(f"{skill}: fewer than 5 quoted trigger phrases")
    words = len(text.split())
    if words >= 3000:
        fail(f"{skill}: {words} words >= 3000")
    for needle, label in [("blocked", "blocked-source procedure"), ("circumvent", "no-circumvention rule"),
                          ("language", "answer in user's language"), ("Not verified", "not-verified statement")]:
        if needle.lower() not in text.lower():
            fail(f"{skill}: missing {label}")


def check_paths() -> None:
    for path in list(ROOT.glob("skills/**/*.md")) + list(ROOT.glob("agents/*.md")) + list(ROOT.glob("references/*.md")):
        for rel in re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w./-]+\.md)", path.read_text(encoding="utf-8")):
            if not (ROOT / rel).exists():
                fail(f"{path.relative_to(ROOT).as_posix()}: broken path {rel}")


def check_license_mentions() -> None:
    for path in [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *ROOT.glob("docs/*.md"), *ROOT.glob("skills/**/*.md"),
                 *ROOT.glob("references/*.md"), ROOT / ".claude-plugin/plugin.json"]:
        text = path.read_text(encoding="utf-8")
        if BANNED.search(text):
            fail(f"{path.relative_to(ROOT).as_posix()}: mentions open source or MIT")
    for path in [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *ROOT.glob("docs/README.*.md")]:
        if "PolyForm Noncommercial" not in path.read_text(encoding="utf-8"):
            fail(f"{path.relative_to(ROOT).as_posix()}: license not named")
    if '"PolyForm-Noncommercial-1.0.0"' not in (ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"):
        fail("plugin.json: license SPDX id missing")


for ref in REFS:
    p = ROOT / "references" / f"{ref}.md"
    check_reference(p) if p.exists() else fail(f"references/{ref}.md missing")
for skill in SKILLS:
    check_skill(skill)
check_paths()
check_license_mentions()

print("\n".join(errors) if errors else "all content checks passed")
sys.exit(1 if errors else 0)
