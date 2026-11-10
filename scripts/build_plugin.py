"""Build dist/pc-hardware-advisor.plugin (a zip of the plugin) without dev-only files."""
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_DIRS = {".git", ".github", "tests", "research", "scripts", "dist", "graphify-out", ".claude", ".codex-plugin", ".agents"}
EXCLUDED_FILES = {"DECISIONS.md", "ORCHESTRATION.md", "REPORT.md", "AUDIT.md", "CLAUDE.md", ".gitignore", "requirements-dev.txt"}
REQUIRED = [".claude-plugin/plugin.json", "README.md", "LICENSE", "CONNECTORS.md", "agents/price-scout.md"]


def included(rel: Path) -> bool:
    return rel.parts[0] not in EXCLUDED_DIRS and rel.name not in EXCLUDED_FILES


def build() -> Path:
    name = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))["name"]
    out = ROOT / "dist" / f"{name}.plugin"
    out.parent.mkdir(exist_ok=True)
    files = sorted(p for p in ROOT.rglob("*") if p.is_file() and included(p.relative_to(ROOT)))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, p.relative_to(ROOT).as_posix())
    # Self-check: required files present, nothing dev-only leaked.
    names = set(zipfile.ZipFile(out).namelist())
    missing = [r for r in REQUIRED if r not in names]
    leaked = [n for n in names if not included(Path(n))]
    skills = [n for n in names if n.startswith("skills/") and n.endswith("/SKILL.md")]
    assert not missing, f"missing: {missing}"
    assert not leaked, f"dev-only files leaked: {leaked}"
    assert len(skills) == 6, f"expected 6 skills, got {skills}"
    print(f"{out} : {len(names)} files, {out.stat().st_size} bytes")
    return out


if __name__ == "__main__":
    sys.exit(0 if build() else 1)
