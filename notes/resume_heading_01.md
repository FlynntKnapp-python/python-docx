# Resume Heading 01

![Resume heading with name, role, and contact info](images/resume_heading_01.png)

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
table = doc.add_table(rows=2, cols=2)
table.cell(0, 0).text = "Flynnt Knapp"
table.cell(1, 0).text = "Django Developer"
table.cell(0, 1).text = "FlynntKnapp@email.app"
table.cell(0, 1).paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
table.cell(1, 1).text = "github.com/FlynntKnapp"
table.cell(1, 1).paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

# Save the document to a .docx file:
saved = utils.save_docx(file_path, doc)
print("Saved: ", saved)
```