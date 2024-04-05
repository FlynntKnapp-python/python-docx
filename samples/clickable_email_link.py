from docx import Document
from docx.oxml.ns import qn
from docx.oxml.shared import OxmlElement

# Specify the file path for the .docx file
file_path = "samples/output/ClickableEmailLink.docx"


def add_email_hyperlink(paragraph, email, display_text):
    # Create the hyperlink tag
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("w:anchor"), email)

    # Set up the display text
    new_run = OxmlElement("w:r")
    text = OxmlElement("w:t")
    text.text = display_text
    new_run.append(text)
    hyperlink.append(new_run)

    # Add the hyperlink to the paragraph
    paragraph._p.append(hyperlink)

    return paragraph


# Usage example
doc = Document()
p = doc.add_paragraph("Please contact us via email: ")
p_email_link = add_email_hyperlink(p, "mailto:email@example.com", "Contact Us")
doc.save(file_path)
