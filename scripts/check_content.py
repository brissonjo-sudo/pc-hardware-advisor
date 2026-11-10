"""Mechanical checks of plugin content (validation gate items that a script can verify).

Usage: python scripts/check_content.py   -> exit 1 on any failure.
"""
import datetime
import json
import re
import sys
from pathlib import Path

import yaml  # PyYAML

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
    """Parse with a real YAML parser: a parse error makes the skill load with empty metadata."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as exc:
        fail(f"frontmatter YAML parse error: {str(exc).splitlines()[0]}")
        return {}
    return {k: str(v) for k, v in (data or {}).items()}


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
    # Official guidance: SKILL.md under 500 lines; the word cap guards context size.
    lines, words = len(text.splitlines()), len(text.split())
    if lines >= 500 or words >= 4000:
        fail(f"{skill}: {lines} lines, {words} words (limits 500 lines, 4000 words)")
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



def prompt_files() -> list[Path]:
    return sorted(ROOT.glob("skills/**/*.md")) + sorted(ROOT.glob("agents/*.md"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_safety_lines() -> None:
    needs = [(r"data,? never as instructions|as data, not", "'data, never as instructions' statement"),
             (r"never (?:buy|purchase)", "'never buy' statement")]
    for path in sorted(ROOT.glob("skills/*/SKILL.md")) + sorted(ROOT.glob("agents/*.md")):
        text = path.read_text(encoding="utf-8")
        for pattern, label in needs:
            if not re.search(pattern, text, re.I):
                fail(f"{rel(path)}: missing {label}")


SELLER_START = re.compile(r"`((?:direct retailer|marketplace|professional refurbisher|manufacturer store|private party"
                          r"|proxy-buying service|seller type unconfirmed)[^`]*)`")


def check_seller_vocab() -> None:
    text = (ROOT / "references/research-method.md").read_text(encoding="utf-8")
    m = re.search(r"^## 5\..*?(?=^## )", text, re.S | re.M)
    canonical = set(re.findall(r"^\|\s*`([^`]+)`", m.group(0), re.M)) if m else set()
    if not canonical:
        fail("research-method.md: no seller-type table found in section 5")
        return
    for path in prompt_files():
        for value in sorted(set(SELLER_START.findall(path.read_text(encoding="utf-8"))) - canonical):
            fail(f"{rel(path)}: seller type `{value}` is not in research-method.md section 5")
    numbers = {"five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}
    count_re = re.compile(r"\b(\d+|" + "|".join(numbers) + r") (?:canonical )?seller types\b", re.I)
    for path in prompt_files():
        for word in count_re.findall(path.read_text(encoding="utf-8")):
            if int(numbers.get(word.lower(), word)) != len(canonical):
                fail(f"{rel(path)}: says {word} seller types, section 5 has {len(canonical)}")


def check_volatile_dates() -> None:
    text = (ROOT / "references/international-buying.md").read_text(encoding="utf-8")
    m = re.search(r"^## Volatile items.*?(?=^## )", text, re.S | re.M)
    if not m:
        fail("international-buying.md: no 'Volatile items' section")
        return
    today = datetime.date.today()
    for row in (r for r in m.group(0).splitlines() if r.startswith("|")):
        if re.search(r"expired|superseded", row, re.I):
            continue
        for d in re.findall(r"(?:until|through|expires)\s+(\d{4}-\d{2}-\d{2})", row, re.I):
            if datetime.date.fromisoformat(d) <= today:
                fail(f"international-buying.md: volatile item date {d} is not after today ({today}): {row[:60]}")


def check_versions() -> None:
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    first = re.search(r"^## \[(\d+\.\d+\.\d+)\]", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
    if not first or first.group(1) != plugin["version"]:
        fail(f"version: plugin.json {plugin['version']} != first CHANGELOG heading {first and first.group(1)}")
    for entry in market.get("plugins", []):
        if entry.get("name") == plugin["name"] and "version" in entry and entry["version"] != plugin["version"]:
            fail(f"version: marketplace.json {entry['version']} != plugin.json {plugin['version']}")
    codex = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    if codex["version"] != plugin["version"]:
        fail(f"version: .codex-plugin/plugin.json {codex['version']} != plugin.json {plugin['version']}")


CITE = re.compile(r"([\w-]+)\.md`?\s+sections?\s+(\d+)(?:\s+(?:and|through|to|&)\s+(\d+))?")


def check_section_citations() -> None:
    targets = {p.name: p for p in [*ROOT.glob("references/*.md"), *ROOT.glob("skills/*/references/*.md")]}
    skipped = set()
    for path in prompt_files():
        for name, *nums in CITE.findall(path.read_text(encoding="utf-8")):
            target = targets.get(f"{name}.md")
            if not target:
                continue
            body = target.read_text(encoding="utf-8")
            if not re.search(r"^## \d+\.", body, re.M):
                skipped.add(target.name)
                continue
            for n in filter(None, nums):
                if not re.search(rf"^## {n}\.", body, re.M):
                    fail(f"{rel(path)}: cites {name}.md section {n}, no '## {n}.' heading there")
    if skipped:
        print(f"note: no numbered headings, citations not checked: {sorted(skipped)}")


GRADER_TYPES = {"llm", "regex", "tool_used", "tool_order", "file_exists", "baseline"}


def check_graders() -> None:
    for case in sorted(p for p in ROOT.glob("tests/cases/*") if p.is_dir()):
        graders = sorted((case / "graders").glob("*.md"))
        if not {"skill-used.md", "no-plugin-skill.md"} & {g.name for g in graders}:
            fail(f"{rel(case)}: no skill-used.md or no-plugin-skill.md grader")
        for g in graders:
            m = re.match(r"^---\n(.*?)\n---\n(.*)$", g.read_text(encoding="utf-8"), re.S)
            try:
                fm = yaml.safe_load(m.group(1)) if m else None
            except yaml.YAMLError:
                fm = None
            if not isinstance(fm, dict):
                fail(f"{rel(g)}: frontmatter missing or unparsable")
                continue
            kind = fm.get("type")
            if kind not in GRADER_TYPES:
                fail(f"{rel(g)}: type {kind!r} not in {sorted(GRADER_TYPES)}")
            if kind == "llm":
                w = fm.get("weight", 1)
                if not (isinstance(w, int) and not isinstance(w, bool) and w > 0):
                    fail(f"{rel(g)}: llm weight must be a positive integer, got {w!r}")
                if not m.group(2).strip():
                    fail(f"{rel(g)}: llm grader has an empty body")
            if kind == "tool_used":
                if not fm.get("tool") or not fm.get("input_match"):
                    fail(f"{rel(g)}: tool_used needs tool and input_match")
                else:
                    try:
                        re.compile(str(fm["input_match"]))
                    except re.error as exc:
                        fail(f"{rel(g)}: input_match does not compile: {exc}")


NUMBER_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]


def heading_count(path: Path) -> int:
    text = re.sub(r"^```.*?^```", "", path.read_text(encoding="utf-8"), flags=re.S | re.M)
    return len(re.findall(r"^#{1,3} \S", text, re.M))


def check_readmes() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    docs = sorted(ROOT.glob("docs/README.*.md"))
    skills, refs = len(list(ROOT.glob("skills/*/SKILL.md"))), len(list(ROOT.glob("references/*.md")))
    for count, phrase in [(skills, "skills"), (refs, "shared references")]:
        if f"{NUMBER_WORDS[count]} {phrase}" not in readme.lower():
            fail(f"README.md: does not state '{NUMBER_WORDS[count]} {phrase}' (real count {count})")
    expected = heading_count(ROOT / "README.md")
    for d in docs:
        if f"docs/{d.name}" not in readme:
            fail(f"README.md: does not link docs/{d.name}")
        if heading_count(d) != expected:
            fail(f"{rel(d)}: {heading_count(d)} headings, README.md has {expected}")
        lines = d.read_text(encoding="utf-8").splitlines()
        if "<!-- language-bar -->" not in lines[:3]:
            fail(f"{rel(d)}: <!-- language-bar --> missing from the first 3 lines")
            continue
        bar = "\n".join(lines[:6])
        for target in ["../README.md"] + [o.name for o in docs if o != d]:
            if f"]({target})" not in bar:
                fail(f"{rel(d)}: language bar does not link {target}")


for ref in REFS:
    p = ROOT / "references" / f"{ref}.md"
    check_reference(p) if p.exists() else fail(f"references/{ref}.md missing")
for skill in SKILLS:
    check_skill(skill)
for agent in sorted(ROOT.glob("agents/*.md")):
    if not frontmatter(agent.read_text(encoding="utf-8")).get("description"):
        fail(f"{agent.name}: frontmatter missing or unparsable")
check_paths()
check_license_mentions()
check_safety_lines()
check_seller_vocab()
check_volatile_dates()
check_versions()
check_section_citations()
check_graders()
check_readmes()

print("\n".join(errors) if errors else "all content checks passed")
sys.exit(1 if errors else 0)
