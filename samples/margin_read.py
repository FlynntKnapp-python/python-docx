# samples\resume_heading.py

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from base import docx_builder
from docx import Document

# Specify the file path for the .docx file:
file_path = "samples/output/MarginRead.docx"

# Load the Document:
doc = docx_builder.manage_docx_file(file_path, "load_or_create")

# Get the first section of the document:
section = doc.sections[0]

# Print the margins:
print("Top Margin:", section.top_margin)
print("Bottom Margin:", section.bottom_margin)
print("Left Margin:", section.left_margin)
print("Right Margin:", section.right_margin)

"""
914400 / 1.0 = 914400 Units/Inch

0.5 Inches - 457200
0.75 Inches - 685800
1.0 Inches - 914400
1.25 Inches - 1143000
1.5 Inches - 1371600
"""
