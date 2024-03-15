from docx import Document

from utils import delete_and_save_docx, create_docx_if_not_exists

# Specify the file path for the .docx file
file_path = "samples/output/Tables.docx"

# Create a new Document
doc_00 = Document()

items = ["Grits", "Gravy", "Buscuits", "Wallets", "Keys", "CPAP", "Glasses"]


# Function to create a 1-row, 3-column table:
# def create_document_table_by_cols(
#     doc: Document, items: list, rows=None, cols=None
# ) -> Document:
#     # Define the number of rows from the length of the items list and the number of columns
#     if len(items) % cols != 0:
#         rows = len(items) // cols + 1
#     else:
#         rows = len(items) // cols

#     # Create a 1-row, 3-column table
#     table = doc.add_table(rows=rows, cols=cols)

#     # Set the text for each cell
#     for i in range(len(items)):
#         table.cell(0, i).text = items[i]
#     # table.cell(0, 0).text = "Left"
#     # table.cell(0, 1).text = "Middle"
#     # table.cell(0, 2).text = "Right"

#     return doc


# # Add a Table to the Document
# doc_01 = create_document_table_by_cols(doc_00, items, cols=3)

# # Create the .docx file if it does not exist
# create_docx_if_not_exists(file_path, doc_01)

# # Delete the file if it exists and save the document to a .docx file
# delete_and_save_docx(file_path, doc_01)


def create_document_table_by_rows(
    doc: Document, items: list, cols=None, rows=None
) -> Document:
    # Define the number of columns from the length of the items list and the number of rows
    if len(items) % rows != 0:
        cols = len(items) // rows + 1
    else:
        cols = len(items) // rows

    # Create the table
    table = doc.add_table(rows=rows, cols=cols)

    # Set the text for each cell
    for i in range(len(items)):
        table.cell(i, 0).text = items[i]

    return doc


# Add a Table to the Document
doc_02 = create_document_table_by_rows(doc_00, items, rows=3)

# Create the .docx file if it does not exist
create_docx_if_not_exists(file_path, doc_02)

# Delete the file if it exists and save the document to a .docx file
delete_and_save_docx(file_path, doc_02)
