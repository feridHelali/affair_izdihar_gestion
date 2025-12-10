#!/usr/bin/env python3
"""
Clean marker-pdf converter – works perfectly with uv
"""

import sys
from pathlib import Path

try:
    from marker.convert import convert_single_pdf
    from marker.models import load_all_models
except ImportError:
    print("\nmarker-pdf is not installed!")
    print("Run:  uv pip install marker-pdf[all]\n")
    sys.exit(1)

from pypdf import PdfReader


def convert(pdf_path: str, output_dir: str = None, chunk_size: int = 10):
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"File not found: {pdf_path}")
        return

    out_dir = Path(output_dir) if output_dir else pdf_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nConverting: {pdf_path.name}")
    print("Loading models (first run = 1–3 min)...")
    models = load_all_models()

    reader = PdfReader(pdf_path)
    total = len(reader.pages)
    print(f"{total} pages → chunk size = {chunk_size}")

    full_md = ""
    images = {}
    counter = 0

    for start in range(0, total, chunk_size):
        pages_to_do = min(chunk_size, total - start)
        print(f"   → pages {start+1}–{start+pages_to_do}")

        md, _, imgs = convert_single_pdf(
            str(pdf_path), models,
            start_page=start, max_pages=pages_to_do,
            batch_multiplier=4  # helps with memory
        )

        # rename images to avoid conflicts
        for old, data in imgs.items():
            new = f"img_{counter:04d}_{old}"
            md = md.replace(f"]({old})", f"]({new})")
            images[new] = data
            counter += 1

        full_md += md + "\n\n---\n\n"

    # save markdown
    md_file = out_dir / f"{pdf_path.stem}.md"
    md_file.write_text(full_md, encoding="utf-8")

    # save images
    if images:
        img_dir = out_dir / f"{pdf_path.stem}_images"
        img_dir.mkdir(exist_ok=True)
        for name, data in images.items():
            path = img_dir / name
            if hasattr(data, "save"):
                data.save(path)
            else:
                path.write_bytes(data)
        print(f"Saved {len(images)} images → {img_dir}")

    print(f"\nSUCCESS → {md_file}")


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("-o", "--output", default=None)
    p.add_argument("--chunk-size", type=int, default=10)
    args = p.parse_args()
    convert(args.input, args.output, args.chunk_size)
