import math

from base import docx_builder
from docx import Document

# Specify the file path for the .docx file:
file_path = "samples/output/MarginSet.docx"

# Load the Document:
doc = docx_builder.manage_docx_file(file_path, "load_or_create")

# Get the first section of the document:
section = doc.sections[0]

# Print the current margins:
print("Top Margin:", section.top_margin)
print("Bottom Margin:", section.bottom_margin)
print("Left Margin:", section.left_margin)
print("Right Margin:", section.right_margin)

# Set margins to 0.5 inches:
doc = docx_builder.set_margins(doc, 0.5, 0.5, 0.5, 0.5)

# Get the first section of the document:
section = doc.sections[0]

# Print the updated margins:
print("Top Margin:", section.top_margin)
print("Bottom Margin:", section.bottom_margin)
print("Left Margin:", section.left_margin)
print("Right Margin:", section.right_margin)

# Set margins to default (1.0) inches:
doc = docx_builder.set_margins(doc)

# Print the updated margins:
print("Top Margin:", section.top_margin)
print("Bottom Margin:", section.bottom_margin)
print("Left Margin:", section.left_margin)
print("Right Margin:", section.right_margin)

# Save the document to a .docx file:
doc.save(file_path)
print("Document saved with specified margins.")
