from docx import Document
import utils

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
doc = utils.add_table(doc, items, cols=3)

# Save the Document:
saved = utils.save_docx(file_path, doc)
