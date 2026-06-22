from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import unittest
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "skills" / "thai-playbook-pdf-builder" / "scripts" / "audit_playbook_package.py"
TEST_TEMP_ROOT = REPO_ROOT / ".test-tmp"
TEST_TEMP_ROOT.mkdir(exist_ok=True)
SPEC = importlib.util.spec_from_file_location("audit_playbook_package", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


@contextmanager
def test_workspace() -> Iterator[Path]:
    path = TEST_TEMP_ROOT / f"case-{uuid.uuid4().hex}"
    path.mkdir()
    try:
        yield path
    finally:
        shutil.rmtree(path, ignore_errors=True)


class AuditPlaybookPackageTests(unittest.TestCase):
    def test_missing_directory_returns_error(self) -> None:
        findings = AUDIT.audit(Path("does-not-exist"))
        self.assertEqual(findings[0].level, "ERROR")

    def test_placeholder_is_reported(self) -> None:
        with test_workspace() as root:
            (root / "source_audit.md").write_text("TODO: complete source audit", encoding="utf-8")
            findings = AUDIT.audit(root)
            messages = "\n".join(item.message for item in findings)
            self.assertIn("Possible placeholders remain", messages)

    def test_strict_mode_exits_nonzero_for_incomplete_package(self) -> None:
        with test_workspace() as root:
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(root), "--strict"],
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("[WARN]", result.stdout)


if __name__ == "__main__":
    unittest.main()
