# samples\resume_heading.py

import utils
from docx import Document

# Specify the file path for the .docx file:
file_path = "samples/output/ResumeHeading.docx"

# Create a new Document:
doc = Document()

# Add a resume heading to the document:
doc = utils.add_resume_heading(doc, "Flynnt Knapp", "Django Developer")

# Save the document to a .docx file:
saved = utils.save_docx(file_path, doc)
print("Saved: ", saved)
