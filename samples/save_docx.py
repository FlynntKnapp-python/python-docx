# samples\save_docx.py

import os

from base import docx_builder
from docx import Document

# Specify the file path for the .docx file:
file_path = os.getenv("SAVE_FILE")

# Create a new Document:
doc = Document()

# Save the empty document to a .docx file:
saved = docx_builder.manage_docx_file(file_path, doc, "save")
print("Saved: ", saved)
