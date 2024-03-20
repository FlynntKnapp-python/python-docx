from docx import Document

from utils import (
    delete_and_save_docx,
    create_docx_if_not_exists,
    add_document_table_by_cols,
)

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

# Create the .docx file if it does not exist
create_docx_if_not_exists(file_path, doc_01)

# Delete the file if it exists and save the document to a .docx file
delete_and_save_docx(file_path, doc_01)
