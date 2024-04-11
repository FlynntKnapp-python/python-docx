# samples\resume_skills.py

from base import docx_builder
from docx import Document

file_path = "samples/output/ResumeSkills.docx"

# Create a new Document:
doc = Document()

# Specify the skills (list) to add to the document:
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
saved = docx_builder.manage_docx_file(file_path, doc, "save")
print("Saved: ", saved)
