# samples\tables.py

from base import docx_builder
from docx import Document

# Specify the file path for the .docx file:
file_path = "samples/output/Tables.docx"

# Create a new empty Document:
doc = Document()

items = [
    "Grits",
    "Gravy",
    "Biscuits",
    "Wallets",
    "Keys",
    "CPAP",
    "Glasses",
    "Phone",
    "Kitten",
    "Pupper",
    "Laptop",
]


# Add a Table to the Document:
doc = docx_builder.add_table(doc, items, cols=3)

# Save the Document:
saved = docx_builder.manage_docx_file(file_path, doc, "save")
print("Saved: ", saved)
