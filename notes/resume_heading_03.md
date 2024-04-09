# Resume Heading 03

![Resume heading with name and role](images/resume_heading_03.png)

```python
# samples\utils.py

from docx import Document
from docx.shared import Pt

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
    name_paragraph = doc.add_paragraph()
    name_run = name_paragraph.add_run(name)
    name_run.font.name = "Arial"
    name_run.font.size = Pt(36)
    title_paragraph = doc.add_paragraph()
    title_run = title_paragraph.add_run(title)
    title_run.font.name = "Arial"
    title_run.font.size = Pt(24)

    return doc
```

```python
# samples\resume_heading.py

import utils
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

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