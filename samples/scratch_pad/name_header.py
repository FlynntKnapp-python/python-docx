# samples\name_header.py

import utils
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

# Specify the file path for the .docx file:
file_path = "samples/output/Name-Header.docx"

# Load the .docx file (instantiating the Document object):
doc = utils.load_or_create_docx(file_path)

# Assign a value to the `name` variable:
name = "Flynnt Knapp"

for i, paragraph in enumerate(doc.paragraphs):
    print(f"paragraph[{i}].text: ", paragraph.text)
    print(f"paragraph[{i}].style.name: ", paragraph.style.name)

# # Add a paragraph to the document with the value of the `name` variable:
# name_paragraph = doc.add_paragraph(name)
# # Align the paragraph to the center:
# name_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER


# utils.delete_and_or_save_docx(file_path, doc)
