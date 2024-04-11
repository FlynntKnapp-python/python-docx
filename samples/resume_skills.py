# samples\resume_skills.py

from base import docx_builder
from docx import Document


def add(file_path="samples/output/ResumeSkills.docx", doc: Document = None):

    if doc is None:
        doc = Document()

    skills = [
        "Git",
        "Scrum",
        "Agile",
        "Python",
        "Django",
        "Django REST",
        "Docker",
        "Linux",
        "S3",
        "Raspberry Pi",
        "Raspberry Pi Pico",
    ]

    # Add a skills table:
    doc = docx_builder.add_table(doc, skills, 3)

    # Save the document to a .docx file:
    saved = docx_builder.save_docx(file_path, doc)
    print("Saved: ", saved)

    return doc


if __name__ == "__main__":
    add()
