import os
from typing import Any

from docx import Document


def delete_and_save_docx(path: str, document: Document):
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
            print(f"Saving the document to {path}...")
            document.save(path)
            print(f"Document saved to {path}.")
        except PermissionError:
            print(f"PermissionError: Unable to delete {path}.")
    else:
        print("The file does not exist.")
