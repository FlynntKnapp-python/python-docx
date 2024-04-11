# samples\resume_heading.py

from base import docx_builder
from docx import Document
import os

file_path = "samples/output/ResumeHeading.docx"

# Create a new Document:
doc = Document()

# Get the name and title from the environment variables:
name = os.getenv("NAME")
title = os.getenv("TITLE")

# Add a resume heading to the document:
doc = docx_builder.add_resume_heading(doc, name, title)

# Save the document to a .docx file:
saved = docx_builder.manage_docx_file(file_path, doc, "save")
print("Saved: ", saved)
