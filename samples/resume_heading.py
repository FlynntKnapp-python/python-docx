# samples\resume_heading.py

from base import docx_builder
from docx import Document

# Specify the file path for the .docx file:
file_path = "samples/output/ResumeHeading.docx"

# Create a new Document:
doc = Document()

# Add a resume heading to the document:
doc = docx_builder.add_resume_heading(doc, "Flynnt Knapp", "Django Developer")

# Save the document to a .docx file:
saved = docx_builder.save_docx(file_path, doc)
print("Saved: ", saved)
