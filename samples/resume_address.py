# samples\resume_address.py

from base import docx_builder
from docx import Document
import os


def add(file_path="samples/output/ResumeAddress.docx", doc: Document = None):

    if doc is None:
        doc = Document()

    address = os.getenv("ADDRESS")
    city = os.getenv("CITY")
    state = os.getenv("STATE")
    zip = os.getenv("ZIP")

    # Add a resume heading to the document:
    doc = docx_builder.add_resume_address(doc, address, city, state, zip)

    # Save the document to a .docx file:
    saved = docx_builder.save_docx(file_path, doc)
    print("Saved: ", saved)

    return doc


if __name__ == "__main__":
    add()
