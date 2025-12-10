#!/usr/bin/env python3
"""
PDF → Markdown converter for uv users (no pip required inside venv)
"""

import sys
from pathlib import Path

# ---- DIRECT IMPORT – will fail with clear message if marker not installed ----
try:
    from marker.convert import convert_single_pdf
    from marker.models import load_all_models
except ImportError:
    print("\n❌ marker-pdf is not installed in this environment.")
    print("   Run this once from your project root:\n")
    print("   uv pip install marker-pdf[all]\n")
    print("   (add torch with CUDA if you have a GPU:)")
    print("   uv pip install marker-pdf[all] torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118\n")
    sys.exit(1)

from pypdf import PdfReader


def convert_pdf_to_markdown(pdf_path: str, output_dir: str = None, chunk_size: int = 10):
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    output_dir = Path(output_dir) if output_dir else pdf_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nConverting: {pdf_path.name}")
    print("Loading models (first run takes 1–3 minutes)...")
    models = load_all_models()

    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Detected {total_pages} pages → processing in chunks of {chunk_size}")

    full_md = ""
    all_images = {}
    img_counter = 0

    for start in range(0, total_pages, chunk_size):
        end = min(start + chunk_size, total_pages)
        print(f"   Pages {start+1}–{end} ...")

        md_chunk, _, images = convert_single_pdf(
            str(pdf_path),
            models,
            start_page=start,
            max_pages=chunk_size
        )

        # Rename images to avoid conflicts
        for old_name, img_data in images.items():
            new_name = f"image_{img_counter:04d}_{old_name}"
            all_images[new_name] = img_data
            md_chunk = md_chunk.replace(f"]({old_name})", f"]({new_name})")
            img_counter += 1

        full_md += md_chunk + "\n\n---\n\n"

    # Save markdown
    md_path = output_dir / f"{pdf_path.stem}.md"
    md_path.write_text(full_md, encoding="utf-8")

    # Save images
    if all_images:
        img_dir = output_dir / f"{pdf_path.stem}_images"
        img_dir.mkdir(exist_ok=True)
        for name, data in all_images.items():
            path = img_dir / name
            if hasattr(data, "save"):
                data.save(path)
            else:
                path.write_bytes(data)

        print(f"Saved {len(all_images)} images → {img_dir}")

    print(f"\nDone! → {md_path}")
    return md_path


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("-o", "--output")
    parser.add_argument("--chunk-size", type=int, default=10)
    args = parser.parse_args()

    convert_pdf_to_markdown(args.input, args.output, args.chunk_size)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("\nUsage: uv run script.py <pdf> -o <folder> --chunk-size 10")
        sys.exit(1)
    main()