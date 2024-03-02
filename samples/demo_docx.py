from docx import Document
from docx.shared import Inches

from utils import delete_and_save_docx, create_docx_if_not_exists

# Specify the file path for the .docx file
file_path = "samples/output/Demo.docx"

document = Document()

document.add_heading("Document Title", 0)

p = document.add_paragraph("A plain paragraph having some ")
p.add_run("bold").bold = True
p.add_run(" and some ")
p.add_run("italic.").italic = True

document.add_heading("Heading, level 1", level=1)
document.add_paragraph("Intense quote", style="Intense Quote")

document.add_paragraph("First item in unordered list", style="List Bullet")
document.add_paragraph("First item in ordered list", style="List Number")
document.add_paragraph("Second item in ordered list", style="List Number")

document.add_picture("images/NoImageAvailable.png", width=Inches(1.25))

records = (
    (3, "101", "Spam"),
    (7, "422", "Eggs"),
    (4, "631", "Spam, spam, eggs, and spam"),
)

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Qty"
hdr_cells[1].text = "Id"
hdr_cells[2].text = "Desc"
for qty, id, desc in records:
    row_cells = table.add_row().cells
    row_cells[0].text = str(qty)
    row_cells[1].text = id
    row_cells[2].text = desc

document.add_page_break()

# Create the .docx file if it does not exist
create_docx_if_not_exists(file_path, document)

# Save the document to a .docx file
delete_and_save_docx(file_path, document)
