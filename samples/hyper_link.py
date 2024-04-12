from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def add_hyperlink(paragraph, url, text, color="0000FF", underline=True):
    """
    A function to add a hyperlink to a paragraph.
    :param paragraph: The paragraph we are adding the hyperlink to.
    :param url: The URL of the hyperlink.
    :param text: The text displayed for the hyperlink.
    :param color: The color of the hyperlink.
    :param underline: If the hyperlink should be underlined.
    """
    # This gets access to the document.xml.rels file and gets a new relation id value
    part = paragraph.part
    r_id = part.relate_to(url, "hyperlink", is_external=True)

    # Create the w:hyperlink tag and add needed values
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(
        qn("r:id"),
        r_id,
    )

    # Create a w:r element
    new_run = OxmlElement("w:r")

    # Create a new w:rPr element
    rPr = OxmlElement("w:rPr")

    # Add color if it is provided
    if color:
        c = OxmlElement("w:color")
        c.set(qn("w:val"), color)
        rPr.append(c)

    # Remove underline if it is requested
    if not underline:
        u = OxmlElement("w:u")
        u.set(qn("w:val"), "none")
        rPr.append(u)

    new_run.append(rPr)
    new_text = OxmlElement("w:t")
    new_text.text = text
    new_run.append(new_text)

    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)

    return hyperlink


# Create a new Document
doc = Document()

# Add a paragraph and insert a hyperlink
p = doc.add_paragraph("Here is an email link: ")
add_hyperlink(p, "mailto:example@example.com", "example@example.com", underline=False)

# Save the document
doc.save("samples/output/HyperLink.docx")
