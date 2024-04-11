# samples\resume_summary.py

from base import docx_builder
from docx import Document
from docx.text.paragraph import Paragraph


def add(paragraph: Paragraph = None) -> Document:

    if paragraph is None:
        doc = Document()

        # Add a horizontal line:
        doc = docx_builder.insert_horizontal_line(doc)

    paragraph = docx_builder.insert_horizontal_line_paragraph_top(paragraph)

    return paragraph


if __name__ == "__main__":
    add()
