# samples\resume_heading.py

from base import docx_builder
from docx import Document
import os


def add(file_path="samples/output/ResumeHeading.docx", doc: Document = None):

    if doc is None:
        doc = Document()

    name = os.getenv("NAME")
    title = os.getenv("TITLE")

    # Add a resume heading to the document:
    doc = docx_builder.add_resume_heading(doc, name, title)

    # Save the document to a .docx file:
    saved = docx_builder.save_docx(file_path, doc)
    print("Saved: ", saved)

    return doc


if __name__ == "__main__":
    add()
