from docx import Document
import math

# Specify the file path for the .docx file:
file_path = "samples/output/MarginSet.docx"

# Create a new Document:
doc = Document()

# Get the first section of the document:
section = doc.sections[0]

# Print the current margins:
print("Top Margin:", section.top_margin)
print("Bottom Margin:", section.bottom_margin)
print("Left Margin:", section.left_margin)
print("Right Margin:", section.right_margin)

"""
0.5 Inches - 457200
0.75 Inches - 685800
1.0 Inches - 914400
1.25 Inches - 1143000
1.5 Inches - 1371600
"""

# 914400 / 1.0 = 914400 Units/Inch
conversion_factor = 914400
section.top_margin = math.floor(0.5 * conversion_factor)
section.bottom_margin = math.floor(0.5 * conversion_factor)
section.left_margin = math.floor(0.5 * conversion_factor)
section.right_margin = math.floor(0.5 * conversion_factor)

# Print the updated margins:
print("Top Margin:", section.top_margin)
print("Bottom Margin:", section.bottom_margin)
print("Left Margin:", section.left_margin)
print("Right Margin:", section.right_margin)

# Save the document to a .docx file:
doc.save(file_path)
print("Document saved with specified margins.")
