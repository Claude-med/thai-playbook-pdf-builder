from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


TEXT_EXTENSIONS = {".md", ".html", ".htm", ".txt", ".json"}

MOJIBAKE_PATTERNS = (
    # Keep these as escapes so the detector is stable across Windows console code pages.
    re.compile("\u0e40\u0e19\u20ac"),
    re.compile("\u0e42\u20ac"),
    re.compile("\u0e40\u0e19[\u0080-\u009f]"),
    re.compile("\u0e42[\u0080-\u009f]"),
    re.compile("\u0e40\u0e18[\u0080-\u009f]"),
    re.compile("\ufffd"),
)

PLACEHOLDER_PATTERN = re.compile(
    r"\b(TODO|TBD|FIXME)\b"
    r"|"
    r"\[(?:[^\]\n]*(?:placeholder|insert|fill|เติม|ใส่|ระบุ|รอข้อมูล)[^\]\n]*)\]",
    re.IGNORECASE,
)


@dataclass
class Finding:
    level: str
    message: str


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def find_first(pattern: str, root: Path) -> Path | None:
    matches = sorted(root.glob(pattern))
    return matches[0] if matches else None


def find_any(patterns: tuple[str, ...], root: Path) -> Path | None:
    for pattern in patterns:
        match = find_first(pattern, root)
        if match is not None:
            return match
    return None


def collect_text(root: Path) -> tuple[str, list[Path]]:
    parts: list[str] = []
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
            parts.append(read_text(path))
    return "\n".join(parts), files


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    low = text.lower()
    return any(term.lower() in low for term in terms)


def missing_terms(text: str, groups: dict[str, tuple[str, ...]]) -> list[str]:
    missing: list[str] = []
    for label, terms in groups.items():
        if not has_any(text, terms):
            missing.append(label)
    return missing


def report_expected_file(findings: list[Finding], label: str, path: Path | None, required: bool = True) -> None:
    if path is None:
        level = "WARN" if required else "INFO"
        findings.append(Finding(level, f"Missing {label}."))
    else:
        findings.append(Finding("OK", f"Found {label}: {path.name}"))


def audit_source_audit(path: Path | None, findings: list[Finding]) -> None:
    if path is None:
        return
    text = read_text(path)
    required = {
        "Big Idea": ("big idea", "แก่น", "ใจความหลัก"),
        "Beginner pain point": ("pain point", "problem", "ปัญหา", "คนอ่านเจอ"),
        "Source evidence": ("source evidence", "timestamp", "ไฟล์", "จากคลิป", "หลักฐาน"),
        "Workflow": ("workflow", "ขั้นตอน", "process", "กระบวนการ"),
        "Examples": ("example", "ตัวอย่าง", "use case", "กรณีใช้"),
        "Warnings / limits": ("warning", "limitation", "ข้อจำกัด", "ความเสี่ยง", "manual review"),
        "Claims to verify": ("claim", "verify", "ตรวจสอบ", "research", "ควรตรวจสอบเพิ่มเติม"),
    }
    for item in missing_terms(text, required):
        findings.append(Finding("WARN", f"source_audit may be missing: {item}."))


def audit_research(path: Path | None, findings: list[Finding]) -> None:
    if path is None:
        return
    text = read_text(path)
    if not re.search(r"https?://", text):
        findings.append(Finding("WARN", "Research notes have no URL."))
    required = {
        "Access date": ("access date", "accessed", "วันที่เข้าถึง"),
        "Used for": ("used for", "verification", "background", "recommendation", "ใช้เพื่อ"),
        "Confidence": ("confidence", "high", "medium", "low", "ความเชื่อมั่น"),
    }
    for item in missing_terms(text, required):
        findings.append(Finding("WARN", f"Research notes may be missing: {item}."))


def audit_blueprint(path: Path | None, findings: list[Finding]) -> None:
    if path is None:
        return
    text = read_text(path)
    required = {
        "Promise": ("promise", "after reading", "หลังอ่าน", "ผู้อ่านจะ"),
        "Problem": ("problem", "pain point", "ปัญหา"),
        "What you can do": ("what you can do", "what you'll build", "สิ่งที่จะได้", "ทำอะไรได้"),
        "Start Here": ("start here", "เริ่มตรงนี้ก่อน"),
        "Before / After": ("before / after", "before after", "ก่อนทำ", "หลังทำ"),
        "Hard Words": ("hard words", "glossary", "ศัพท์ยาก", "ภาษาคน"),
        "Simplest Example": ("simplest example", "tiny example", "ตัวอย่างง่าย"),
        "Quick Win": ("quick win", "10-15", "15-minute"),
        "5-Step Method": ("5-step", "5 step", "วิธีทำ", "ขั้น"),
        "Full Worked Example": ("full worked example", "worked example", "ตัวอย่างเต็ม"),
        "Copy Box": ("copy box", "copy-ready", "prompt ready", "นำไปใช้ต่อ"),
        "Fix Guide": ("fix guide", "ถ้าทำไม่ได้", "แก้แบบนี้"),
        "Cheat Sheet": ("cheat sheet", "สรุปทั้งเล่ม", "หน้าเดียว"),
        "Good vs Weak": ("good output", "weak output", "ผลลัพธ์ที่ดี", "ผลลัพธ์ที่อ่อน"),
        "Source Credit": ("source credit", "แหล่งที่มา", "ที่มาของข้อมูล"),
    }
    for item in missing_terms(text, required):
        findings.append(Finding("WARN", f"playbook_blueprint may be missing: {item}."))


def audit_credit(path: Path | None, findings: list[Finding]) -> None:
    if path is None:
        return
    text = read_text(path)
    if not re.search(r"https?://", text):
        findings.append(Finding("WARN", "Source credit file has no URL."))
    if not has_any(text, ("access", "accessed", "access date", "วันที่เข้าถึง")):
        findings.append(Finding("WARN", "Source credit file may be missing access date."))
    if not has_any(text, ("creator", "channel", "ผู้สร้าง", "ช่อง")):
        findings.append(Finding("WARN", "Source credit file may be missing creator/channel."))
    if not has_any(text, ("Claude Work TH", "application", "ประยุกต์")):
        findings.append(Finding("WARN", "Source credit file may be missing Claude Work TH application note."))


def audit(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    if not root.exists():
        return [Finding("ERROR", f"Output directory does not exist: {root}")]

    source_audit = find_any(("source_audit*.md", "*source-audit*.md"), root)
    blueprint = find_any(("playbook_blueprint*.md", "*blueprint*.md"), root)
    pdf = find_first("*playbook*.pdf", root)
    editable = find_any(("*playbook*.html", "*playbook*.md", "playbook_final.md"), root)
    caption = find_first("*facebook_caption*.md", root)
    carousel = find_first("*carousel_outline*.md", root)
    credit = find_first("*source_credit*.md", root)
    prompt_pack = find_first("*prompt_pack*.md", root)
    research = find_any(("*research_notes*.md", "*research_brief*.md"), root)

    report_expected_file(findings, "source audit", source_audit, required=True)
    report_expected_file(findings, "research notes", research, required=False)
    report_expected_file(findings, "playbook blueprint", blueprint, required=True)
    report_expected_file(findings, "playbook PDF", pdf, required=False)
    report_expected_file(findings, "editable playbook source", editable, required=True)
    report_expected_file(findings, "Facebook caption", caption, required=False)
    report_expected_file(findings, "carousel outline", carousel, required=False)
    report_expected_file(findings, "source credit", credit, required=True)
    report_expected_file(findings, "prompt pack", prompt_pack, required=False)

    text, files = collect_text(root)
    if not files:
        findings.append(Finding("WARN", "No readable text files found for content checks."))
        return findings

    for pattern in MOJIBAKE_PATTERNS:
        hits = pattern.findall(text)
        if hits:
            findings.append(Finding("WARN", f"Possible mojibake pattern `{pattern.pattern}` appears {len(hits)} time(s)."))

    package_terms = {
        "Problem This Playbook Solves": ("problem this playbook solves", "ปัญหา", "ช่วยแก้"),
        "What You Can Do After Reading": ("what you can do", "what you'll build", "ทำอะไรได้", "สิ่งที่จะได้"),
        "Start Here": ("start here", "เริ่มตรงนี้ก่อน"),
        "Before / After": ("before / after", "before after", "ก่อนทำ", "หลังทำ"),
        "Hard Words In Plain Thai": ("hard words", "plain thai", "ศัพท์ยาก", "ภาษาคน"),
        "Simplest Example First": ("simplest example", "tiny example", "ตัวอย่างง่าย"),
        "What To Prepare": ("what to prepare", "before starting", "เตรียม", "ก่อนเริ่ม"),
        "Quick Win": ("quick win", "10-15", "15-minute"),
        "5-Step Method": ("5-step", "5 step", "วิธีทำ", "ขั้นที่"),
        "Step Pages": ("ขั้นที่", "step 1", "step 2"),
        "Full Worked Example": ("full worked example", "worked example", "ตัวอย่างเต็ม"),
        "Copy Box": ("copy box", "copy-ready", "prompt ready", "นำไปใช้ต่อ"),
        "Fix Guide": ("fix guide", "ถ้าทำไม่ได้", "แก้แบบนี้"),
        "Good vs Weak": ("good output", "weak output", "ผลลัพธ์ที่ดี", "ผลลัพธ์ที่อ่อน"),
        "Decision Guide": ("decision guide", "choose", "เลือก"),
        "Common Mistakes": ("common mistakes", "mistake", "ข้อผิดพลาด"),
        "Cheat Sheet": ("cheat sheet", "สรุปทั้งเล่ม", "หน้าเดียว"),
        "Action Plan": ("7-day", "action plan", "next action", "แผน"),
        "Source Credit": ("source credit", "แหล่งที่มา", "ที่มาของข้อมูล"),
    }
    for label in missing_terms(text, package_terms):
        findings.append(Finding("WARN", f"Missing or hard-to-detect section: {label}."))

    if has_any(text, ("official", "docs", "documentation", "ข้อมูลเสริม", "external")) and research is None:
        findings.append(Finding("WARN", "External/source context found but no research notes file detected."))

    if has_any(text, ("ai", "claude", "codex", "prompt", "agent", "workflow")) and prompt_pack is None:
        findings.append(Finding("INFO", "AI/workflow terms found but no separate prompt pack detected. This is OK for PDF-only jobs if copy boxes are inside the PDF."))

    audit_source_audit(source_audit, findings)
    audit_research(research, findings)
    audit_blueprint(blueprint, findings)
    audit_credit(credit, findings)

    placeholder_hits: list[str] = []
    for path in files:
        file_text = read_text(path)
        if PLACEHOLDER_PATTERN.search(file_text):
            placeholder_hits.append(path.name)
    if placeholder_hits:
        findings.append(Finding("WARN", "Possible placeholders remain in: " + ", ".join(sorted(set(placeholder_hits)))))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a Thai Simple Action Playbook output package.")
    parser.add_argument("outputs_dir", type=Path, help="Directory containing playbook outputs.")
    parser.add_argument("--strict", action="store_true", help="Exit 1 when warnings or errors are found.")
    args = parser.parse_args()

    findings = audit(args.outputs_dir)
    for finding in findings:
        print(f"[{finding.level}] {finding.message}")

    has_problem = any(item.level in {"WARN", "ERROR"} for item in findings)
    if args.strict and has_problem:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
