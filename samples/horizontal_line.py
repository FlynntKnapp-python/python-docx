# samples\horizontal_line.py

from base import docx_builder
from docx import Document

# Specify the file path for the .docx file:
file_path = "samples/output/HorizontalLine.docx"

# Create a new Document:
doc = Document()

# Add a paragraph that will contain the horizontal line:
paragraph = doc.add_paragraph()
paragraph.add_run("This is the text above the first line.")

# Add a horizontal line:
paragraph = docx_builder.insert_horizontal_line_paragraph(paragraph)

# Add another paragraph after the line:
paragraph_after = doc.add_paragraph("This is the text below the first line.")

# Add another horizontal line:
doc = docx_builder.insert_horizontal_line(doc)

# Add another paragraph after the line:
paragraph_after = doc.add_paragraph("This is the text below the second line.")

# Save the document:
saved = docx_builder.save_docx(file_path, doc)
print("Saved: ", saved)
