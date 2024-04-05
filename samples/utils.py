import os
from typing import Any

from docx import Document


def load_docx_if_exists(path: str) -> Document:
    """
    Load a .docx file if it exists.

    Parameters:
    - path (str): The file system path where the .docx file is saved.

    Returns:
    - Document: The docx.Document object representing the .docx file.
    """
    if os.path.exists(path):
        print(f"Loading {path}...")
        document = Document(path)
        print(f"Document loaded from {path}.")
        return document
    else:
        print(f"The file {path} does not exist.")
        return Document()


# Function to create a table by number of columns:
def add_document_table_by_cols(doc: Document, items: list, cols=None) -> Document:
    """
    Create a table in a Word document with a specified number of columns.

    Args:
    - doc (Document): The docx.Document object to which the table will be added.
    - items (list): The list of items to be added to the table.
    - cols (int): The number of columns in the table.

    Returns:
    - Document: The docx.Document object with the table added.
    """
    if len(items) % cols != 0:
        rows = len(items) // cols + 1
    else:
        rows = len(items) // cols

    # Create a 1-row, 3-column table
    table = doc.add_table(rows=rows, cols=cols)

    # Set the text for each cell
    for i in range(len(items)):
        table.cell(0, i).text = items[i]

    return doc


def create_docx_if_not_exists(path: str, document: Any):
    """
    Create a .docx file if it does not exist.

    Parameters:
    - path (str): The file system path where the .docx file is saved. If the file exists, it will not be created.
    - document (Any): The object to be saved. This object represents a Word document.

    Returns:
    - None
    """
    if not os.path.exists(path):
        print(f"Creating {path}...")
        document.save(path)
        print(f"Document created at {path}.")
    else:
        print(f"The file {path} already exists.")


def delete_and_or_save_docx(path: str, document: Document):
    """
    Delete the file if it exists and save the document to a .docx file.

    Parameters:
    - path (str): The file system path where the .docx file is saved. If the file exists, it will be deleted before saving.
    - document (Document): The docx.Document object to be saved. This object represents a Word document.

    Returns:
    - None
    """
    # Check if the file exists to avoid FileNotFoundError
    if os.path.exists(path):
        # Delete the file
        print(f"Deleting {path}...")
        try:
            os.remove(path)
            print(f"File {path} deleted.")
        except PermissionError:
            print(f"PermissionError: Unable to delete {path}.")
    else:
        print("The file does not exist.")
    # Save the document to the specified path
    print(f"Saving the document to {path}...")
    document.save(path)
    print(f"Document saved to {path}.")


def return_object_attributes(obj: Any):
    """
    Return the attributes of an object.

    Parameters:
    - obj (Any): The object for which to return attributes.

    Returns:
    - list: The list of attributes of the object.
    """
    return dir(obj)


def enumerate_paragraphs(doc: Document):
    """
    Returns an enumerated list of paragraphs in a Word document.

    Parameters:
    - doc (Document): The docx.Document object representing the Word document.

    Returns:
    - list: The enumerated list of paragraphs in the document.
    """
    return [(i, paragraph.text) for i, paragraph in enumerate(doc.paragraphs)]


def print_attributes_to_console(obj: object):
    """
    Print the attributes of an object to the console.

    Args:
    - obj: The object for which to list attributes.

    Returns:
    - None
    """
    print(f"List of {obj} Attributes:")
    for attr in dir(obj):
        print(f"\t{attr}")

    return None
