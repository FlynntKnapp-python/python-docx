# samples\save_docx.py

import os

from base import docx_builder
from docx import Document

# Specify the file path for the .docx file:
file_path = os.getenv("SAVE_DOCX_FILE")

# Create a new Document:
doc = Document()

# Save the empty document to a .docx file:
saved = docx_builder.save_docx(file_path, doc)
print("Saved: ", saved)
