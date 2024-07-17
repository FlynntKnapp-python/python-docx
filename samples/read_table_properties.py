# samples\read_table_properties.py

import os

from base import docx_builder

# Specify the file path for the .docx file:
file_path = os.getenv("READ_TABLE_PROPERTIES")

# Load or create the Document:
doc = docx_builder.manage_docx_file(file_path, "load_or_create")


# Iterate through each table in the document
for table in doc.tables:
    # Iterate through each row in the table
    for row in table.rows:
        # Iterate through each cell in the row
        for cell in row.cells:
            # Print the text content of the cell
            print(cell.text)

# Save the document to a .docx file:
saved = docx_builder.manage_docx_file(file_path, doc, "save")
print("Saved: ", saved)
