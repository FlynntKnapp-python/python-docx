from docx import Document

from utils import (
    delete_and_save_docx,
    create_docx_if_not_exists,
    add_document_table_by_cols,
)

# Specify the file path for the .docx file
file_path = "samples/output/ParaTablePara.docx"

paragraph_text_01 = (
    "This is the first paragraph of text that is being added to the document."
)
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

paragraph_text_02 = (
    "This is the second paragraph of text that is being added to the document."
)


# Create a new Document
doc = Document()

# Add a paragraph of text
p1 = doc.add_paragraph(paragraph_text_01)

# Add a Table to the Document
doc = add_document_table_by_cols(doc, items, cols=4)

# Add a paragraph of text
p2 = doc.add_paragraph(paragraph_text_02)

# Create the .docx file if it does not exist
create_docx_if_not_exists(file_path, doc)

# Delete the file if it exists and save the document to a .docx file
delete_and_save_docx(file_path, doc)
