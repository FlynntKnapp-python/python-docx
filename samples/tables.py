from docx import Document
from utils import (add_document_table_by_cols, create_docx_if_not_exists,
                   delete_and_or_save_docx)

# Specify the file path for the .docx file
file_path = "samples/output/Tables.docx"

# Create a new Document
doc_00 = Document()

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


# Add a Table to the Document
doc_01 = add_document_table_by_cols(doc_00, items, cols=4)

# Delete the file if it exists and save the document to a .docx file
delete_and_or_save_docx(file_path, doc_01)
