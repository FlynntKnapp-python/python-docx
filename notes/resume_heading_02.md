# Resume Heading 02

![Resume heading with name and role](images/resume_heading_02.png)

```python
# samples\utils.py

from docx import Document

def add_resume_heading_as_table(doc: Document, name: str, title: str) -> Document:
    """
    Add a heading to a resume document as a table.

    Parameters:
    - doc (Document): The Document object to add the heading to.
    - name (str): The name to add to the heading.
    - title (str): The title to add to the heading.

    Returns:
    - Document: The modified Document object.
    """
    table = doc.add_table(rows=2, cols=1)
    table.cell(0, 0).text = name
    table.cell(1, 0).text = title

    return doc
```

```python
# samples\resume_heading.py

import utils
from docx import Document

# Specify the file path for the .docx file:
file_path = "samples/output/ResumeHeading.docx"

# Create a new Document:
doc = Document()

# Add a resume heading to the document:
doc = utils.add_resume_heading_as_table(doc, "Flynnt Knapp", "Django Developer")

# Save the document to a .docx file:
saved = utils.save_docx(file_path, doc)
print("Saved: ", saved)
```
