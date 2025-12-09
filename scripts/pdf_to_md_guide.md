Features:

📄 Converts PDFs to Markdown with high fidelity (tables, images, equations)
🖼️ Extracts and saves images separately
📚 Batch processing for multiple PDFs
🎯 Simple CLI interface

Usage:
```bash
Install dependencies first
pip install marker-pdf

# Convert single PDF
python script.py document.pdf

# Convert all PDFs in a folder
python script.py /path/to/pdf/folder/


# Specify output directory
python script.py document.pdf -o output_folder/
```
First run will take a bit longer as Marker downloads AI models (~1-2GB), but after that it's fast and reuses the cached models.
For your Sage docs, this should handle tables, structured data, and formatting really well. Give it a shot and let me know if you need any tweaks! 💪