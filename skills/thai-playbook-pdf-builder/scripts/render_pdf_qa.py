from __future__ import annotations

import argparse
import re
from pathlib import Path


GENERATED_PAGE_PATTERN = re.compile(r"page-\d+\.png")


def prepare_output_directory(out_dir: Path, force: bool) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    generated = [
        path
        for path in out_dir.iterdir()
        if path.is_file()
        and (GENERATED_PAGE_PATTERN.fullmatch(path.name) or path.name == "contact_sheet.jpg")
    ]
    if generated and not force:
        raise SystemExit(
            f"Output directory already contains rendered QA files: {out_dir}. "
            "Use --force to replace only page-NN.png and contact_sheet.jpg files."
        )
    for path in generated:
        path.unlink()


def render_pdf(pdf_path: Path, out_dir: Path, scale: float, force: bool = False) -> list[Path]:
    try:
        import pypdfium2 as pdfium
        from PIL import Image, ImageDraw
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency. Install pypdfium2 and Pillow, or use an existing project environment that has them."
        ) from exc

    if not pdf_path.exists():
        raise SystemExit(f"PDF does not exist: {pdf_path}")

    if scale <= 0:
        raise SystemExit("Render scale must be greater than zero.")

    prepare_output_directory(out_dir, force)
    doc = pdfium.PdfDocument(str(pdf_path))
    page_paths: list[Path] = []

    try:
        for index in range(len(doc)):
            page = doc[index]
            bitmap = page.render(scale=scale)
            image = bitmap.to_pil()
            page_path = out_dir / f"page-{index + 1:02d}.png"
            image.save(page_path)
            image.close()
            bitmap.close()
            page.close()
            page_paths.append(page_path)
    finally:
        doc.close()

    if page_paths:
        thumbs = []
        thumb_width = 320
        gutter = 18
        label_height = 28
        columns = 3
        for page_path in page_paths:
            with Image.open(page_path) as source:
                image = source.convert("RGB")
                ratio = thumb_width / image.width
                thumb_height = int(image.height * ratio)
                thumb = image.resize((thumb_width, thumb_height))
                image.close()
            canvas = Image.new("RGB", (thumb_width, thumb_height + label_height), "white")
            canvas.paste(thumb, (0, label_height))
            thumb.close()
            draw = ImageDraw.Draw(canvas)
            draw.text((8, 6), page_path.stem, fill=(20, 20, 20))
            thumbs.append(canvas)

        rows = (len(thumbs) + columns - 1) // columns
        sheet_width = columns * thumb_width + (columns + 1) * gutter
        sheet_height = rows * thumbs[0].height + (rows + 1) * gutter
        sheet = Image.new("RGB", (sheet_width, sheet_height), (235, 235, 235))

        for idx, thumb in enumerate(thumbs):
            row = idx // columns
            col = idx % columns
            x = gutter + col * (thumb_width + gutter)
            y = gutter + row * (thumb.height + gutter)
            sheet.paste(thumb, (x, y))

        sheet.save(out_dir / "contact_sheet.jpg", quality=92)
        sheet.close()
        for thumb in thumbs:
            thumb.close()

    return page_paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Render PDF pages for visual QA.")
    parser.add_argument("pdf", type=Path, help="PDF file to render.")
    parser.add_argument("--out", type=Path, required=True, help="Output directory for rendered pages.")
    parser.add_argument("--scale", type=float, default=2.0, help="Render scale. Default: 2.0")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace only page-NN.png and contact_sheet.jpg files created by this script.",
    )
    args = parser.parse_args()

    pages = render_pdf(args.pdf, args.out, args.scale, force=args.force)
    print(f"Rendered {len(pages)} page(s) to {args.out}")
    if pages:
        print(f"Contact sheet: {args.out / 'contact_sheet.jpg'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
