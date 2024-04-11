# samples\margin_adjust.py

from base import docx_builder
from docx import Document

# Specify the file path for the .docx file:
file_path = "samples/output/MarginAdjust.docx"

# Create a new (empty) Document:
doc = Document()

# Add a resume heading to the document:
doc = docx_builder.add_resume_heading(doc, "Flynnt Knapp", "Django Developer")

section = doc.sections[0]

# Set the margins (1 inch = 914400 Units)
inch = 914400
section.top_margin = 1 * inch
section.bottom_margin = 1 * inch
section.left_margin = 1 * inch
section.right_margin = 1 * inch

print("Top Margin:", section.top_margin)
print("Bottom Margin:", section.bottom_margin)
print("Left Margin:", section.left_margin)
print("Right Margin:", section.right_margin)


# Save the document to a .docx file:
saved = docx_builder.manage_docx_file(file_path, doc, "save")
print("Saved: ", saved)
