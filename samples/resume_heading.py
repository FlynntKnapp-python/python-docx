# samples\resume_heading.py

from base import docx_builder
from docx import Document
import os

# Specify the file path for the .docx file:
file_path = "samples/output/ResumeHeading.docx"

# Create a new Document:
doc = Document()

name = os.getenv("NAME")
title = os.getenv("TITLE")
address = os.getenv("ADDRESS")
city = os.getenv("CITY")
state = os.getenv("STATE")
zip = os.getenv("ZIP")

# Add a resume heading to the document:
doc = docx_builder.add_resume_heading(doc, name, title)

# Save the document to a .docx file:
saved = docx_builder.save_docx(file_path, doc)
print("Saved: ", saved)
