# Resume Heading 00

![Resume Heading with Name and Role](images/resume_heading_00.png)

```python
# samples\utils.py

from docx import Document

def add_resume_heading(doc: Document, name: str, title: str) -> Document:
    """
    Add a heading to a resume document.

    Parameters:
    - doc (Document): The Document object to add the heading to.
    - name (str): The name to add to the heading.
    - title (str): The title to add to the heading.

    Returns:
    - Document: The modified Document object.
    """
    doc.add_paragraph(name).style = "Title"
    doc.add_paragraph(title).style = "Subtitle"

    return doc
```

```python
# samples\resume_heading.py

from docx import Document
import utils

# Specify the file path for the .docx file:
file_path = "samples/output/ResumeHeading.docx"

# Create a new Document:
doc = Document()

# Add a resume heading to the document:
doc = utils.add_resume_heading(doc, "Flynnt Knapp", "Django Developer")

# Save the document to a .docx file:
saved = utils.save_docx(file_path, doc)
print("Saved: ", saved)
```
