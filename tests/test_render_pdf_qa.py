from __future__ import annotations

import importlib.util
import shutil
import sys
import unittest
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from PIL import Image


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "skills" / "thai-playbook-pdf-builder" / "scripts" / "render_pdf_qa.py"
TEST_TEMP_ROOT = REPO_ROOT / ".test-tmp"
TEST_TEMP_ROOT.mkdir(exist_ok=True)
SPEC = importlib.util.spec_from_file_location("render_pdf_qa", SCRIPT)
assert SPEC and SPEC.loader
RENDER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = RENDER
SPEC.loader.exec_module(RENDER)


@contextmanager
def test_workspace() -> Iterator[Path]:
    path = TEST_TEMP_ROOT / f"case-{uuid.uuid4().hex}"
    path.mkdir()
    try:
        yield path
    finally:
        shutil.rmtree(path, ignore_errors=True)


class RenderPdfQaTests(unittest.TestCase):
    def create_pdf(self, path: Path) -> None:
        image = Image.new("RGB", (320, 480), "white")
        image.save(path, "PDF")
        image.close()

    def test_render_and_safe_force_replace(self) -> None:
        with test_workspace() as root:
            pdf_path = root / "sample.pdf"
            out_dir = root / "qa output"
            self.create_pdf(pdf_path)

            pages = RENDER.render_pdf(pdf_path, out_dir, 1.0)
            self.assertEqual(len(pages), 1)
            self.assertTrue((out_dir / "page-01.png").is_file())
            self.assertTrue((out_dir / "contact_sheet.jpg").is_file())

            keep = out_dir / "review-notes.txt"
            keep.write_text("keep", encoding="utf-8")
            with self.assertRaises(SystemExit):
                RENDER.render_pdf(pdf_path, out_dir, 1.0)

            RENDER.render_pdf(pdf_path, out_dir, 1.0, force=True)
            self.assertEqual(keep.read_text(encoding="utf-8"), "keep")

    def test_invalid_scale_is_rejected(self) -> None:
        with test_workspace() as root:
            pdf_path = root / "sample.pdf"
            self.create_pdf(pdf_path)
            with self.assertRaises(SystemExit):
                RENDER.render_pdf(pdf_path, root / "qa", 0)


if __name__ == "__main__":
    unittest.main()
