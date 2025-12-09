#!/usr/bin/env python3
"""
High-Fidelity PDF to Markdown Converter using Marker
Handles tables, images, equations, and complex layouts
"""

import os
import sys
from pathlib import Path

def install_marker():
    """Install marker-pdf if not already installed"""
    try:
        from marker.converters.pdf import PdfConverter
        print("✓ Marker already installed")
        return True
    except ImportError:
        print("Installing marker-pdf... (this may take a minute)")
        os.system(f"{sys.executable} -m pip install marker-pdf --quiet")
        try:
            from marker.converters.pdf import PdfConverter
            print("✓ Marker installed successfully")
            return True
        except ImportError:
            print("❌ Failed to import marker. Trying alternative installation...")
            os.system(f"{sys.executable} -m pip install 'marker-pdf[all]' --quiet")
            return False

def convert_pdf_to_markdown(pdf_path, output_dir=None):
    """
    Convert a PDF file to Markdown with high fidelity
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Optional output directory (defaults to same as PDF)
    
    Returns:
        Path to the generated markdown file
    """
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered
    
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    
    # Set output directory
    if output_dir is None:
        output_dir = pdf_path.parent
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📄 Converting: {pdf_path.name}")
    print("⏳ Loading AI models (first run takes longer)...")
    
    # Initialize converter with models
    converter = PdfConverter(artifact_dict=create_model_dict())
    
    print("🔄 Processing PDF...")
    
    # Convert PDF
    rendered = converter(str(pdf_path))
    
    # Extract text/markdown
    markdown_text, _, images = text_from_rendered(rendered)
    
    # Save markdown file
    md_filename = pdf_path.stem + ".md"
    md_path = output_dir / md_filename
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_text)
    
    # Save images if any
    if images:
        img_dir = output_dir / f"{pdf_path.stem}_images"
        img_dir.mkdir(exist_ok=True)
        
        saved_count = 0
        for img_name, img_data in images.items():
            try:
                img_path = img_dir / img_name
                # Handle both PIL images and bytes
                if hasattr(img_data, 'save'):
                    img_data.save(img_path)
                else:
                    with open(img_path, 'wb') as f:
                        f.write(img_data)
                saved_count += 1
            except Exception as e:
                print(f"⚠️  Could not save image {img_name}: {e}")
        
        if saved_count > 0:
            print(f"🖼️  Saved {saved_count} images to: {img_dir}")
    
    print(f"✅ Conversion complete!")
    print(f"📝 Markdown saved to: {md_path}")
    
    return md_path

def batch_convert(input_dir, output_dir=None):
    """
    Convert all PDFs in a directory
    
    Args:
        input_dir: Directory containing PDF files
        output_dir: Optional output directory
    """
    input_dir = Path(input_dir)
    pdf_files = list(input_dir.glob("*.pdf")) + list(input_dir.glob("*.PDF"))
    
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return
    
    print(f"\n📚 Found {len(pdf_files)} PDF file(s)")
    
    success_count = 0
    error_count = 0
    
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"\n{'='*60}")
        print(f"Processing {i}/{len(pdf_files)}")
        try:
            convert_pdf_to_markdown(pdf_path, output_dir)
            success_count += 1
        except Exception as e:
            print(f"❌ Error converting {pdf_path.name}: {e}")
            error_count += 1
            continue
    
    print(f"\n{'='*60}")
    print(f"🏁 Batch conversion complete!")
    print(f"✅ Successful: {success_count}")
    print(f"❌ Failed: {error_count}")

def main():
    """Main function with CLI interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown with high fidelity using Marker"
    )
    parser.add_argument(
        "input",
        help="Path to PDF file or directory containing PDFs"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output directory (default: same as input)",
        default=None
    )
    parser.add_argument(
        "--install",
        action="store_true",
        help="Install marker-pdf and exit"
    )
    
    args = parser.parse_args()
    
    # Install if requested
    if args.install:
        install_marker()
        return
    
    # Ensure marker is installed
    if not install_marker():
        print("\n❌ Could not verify marker installation.")
        print("Try manually: pip install marker-pdf")
        sys.exit(1)
    
    input_path = Path(args.input)
    
    # Check if input is file or directory
    if input_path.is_file():
        convert_pdf_to_markdown(input_path, args.output)
    elif input_path.is_dir():
        batch_convert(input_path, args.output)
    else:
        print(f"❌ Invalid input: {input_path}")
        sys.exit(1)

if __name__ == "__main__":
    # Simple usage examples
    if len(sys.argv) == 1:
        print("\n🚀 PDF to Markdown Converter (Marker)\n")
        print("Usage:")
        print("  python script.py document.pdf              # Convert single PDF")
        print("  python script.py /path/to/pdfs/            # Convert all PDFs in folder")
        print("  python script.py document.pdf -o output/   # Specify output directory")
        print("  python script.py --install                 # Install dependencies\n")
        sys.exit(0)
    
    main()