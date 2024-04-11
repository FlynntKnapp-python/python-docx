# samples\horizontal_line.py

from base import docx_builder
from docx import Document
from docx.text.paragraph import Paragraph


def add(
    file_path="samples/output/HorizontalLine.docx", paragraph: Paragraph = None
) -> Document:

    if paragraph is None:
        doc = Document()

    # Add a horizontal line:
    doc = docx_builder.insert_horizontal_line(doc)

    # Save the document:
    saved = docx_builder.save_docx(file_path, doc)
    print("Saved: ", saved)

    return doc


if __name__ == "__main__":
    add()
