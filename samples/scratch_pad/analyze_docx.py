# samples\analyze_docx.py

import utils
from docx import Document

# Specify the file path for the .docx file:
file_path = "samples\output\BruceStull-Resume.docx"

# Load the .docx file (instantiating the Document object):
doc = utils.load_or_create_docx(file_path)

# Get the paragraphs of the document:
paragraphs = doc.paragraphs

# Get the number of paragraphs in the document:
num_paragraphs = len(paragraphs)
# Print the number of paragraphs in the document:
print(f"Number of Paragraphs: {num_paragraphs}")

for i, paragraph in enumerate(paragraphs):
    print(f"paragraph[{i}].text: ", paragraph.text)


# `run` attributes:
"""
run.text
run.bold
run.italic
run.underline
run.font.name
run.font.size
run.font.color.rgb
run.font.bold
run.font.italic
run.font.underline
run.font.strike
run.font.subscript
run.font.superscript
run.font.all_caps
run.font.hidden
run.font.highlight_color
run.font.shadow
run.font.size
"""
