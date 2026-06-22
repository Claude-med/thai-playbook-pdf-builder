from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "thai-playbook-pdf-builder"
TEXT_EXTENSIONS = {".html", ".md", ".py", ".txt", ".yaml", ".yml"}
MOJIBAKE_PATTERNS = ("\ufffd", "\u0e40\u0e19\u20ac", "\u0e42\u20ac")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        raw, _body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter is not closed") from exc

    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def validate() -> list[str]:
    errors: list[str] = []
    skill_md = SKILL_ROOT / "SKILL.md"
    if not skill_md.is_file():
        return [f"Missing {skill_md.relative_to(REPO_ROOT)}"]

    try:
        skill_text = skill_md.read_text(encoding="utf-8")
        fields = parse_frontmatter(skill_text)
    except (UnicodeDecodeError, ValueError) as exc:
        return [str(exc)]

    if set(fields) != {"name", "description"}:
        errors.append("SKILL.md frontmatter must contain only name and description")
    name = fields.get("name", "")
    if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
        errors.append("Skill name must use lowercase letters, digits, and hyphens")
    if name != SKILL_ROOT.name:
        errors.append("Skill folder name must match frontmatter name")
    if not fields.get("description"):
        errors.append("Skill description must not be empty")
    if len(skill_text.splitlines()) >= 500:
        errors.append("SKILL.md must stay under 500 lines")

    required = (
        "agents/openai.yaml",
        "assets/a4-playbook-template.html",
        "scripts/audit_playbook_package.py",
        "scripts/render_pdf_qa.py",
    )
    for relative in required:
        if not (SKILL_ROOT / relative).is_file():
            errors.append(f"Missing required skill file: {relative}")

    reference_links = re.findall(r"`(references/[^`]+)`", skill_text)
    for relative in reference_links:
        if not (SKILL_ROOT / relative).is_file():
            errors.append(f"Broken SKILL.md reference: {relative}")

    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"Not valid UTF-8: {path.relative_to(REPO_ROOT)} ({exc})")
            continue
        for pattern in MOJIBAKE_PATTERNS:
            if pattern in text:
                errors.append(f"Possible mojibake in {path.relative_to(REPO_ROOT)}: {pattern!r}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            fail(error)
        return 1
    print(f"Skill is valid: {SKILL_ROOT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
