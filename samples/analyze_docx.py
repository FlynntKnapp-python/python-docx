# samples\analyze_docx.py

from docx import Document

# Use `enumerate_paragraphs` to print the number and text of each paragraph in the document:
from utils import enumerate_paragraphs

# Specify the file path for the .docx file:
file_path = "samples/output/BruceStull-Resume.docx"

# Load the .docx file (instantiating the Document object):
doc = Document(file_path)

# Get the number of paragraphs in the document:
num_paragraphs = len(doc.paragraphs)

# Print the number of paragraphs in the document:
print(f"Number of Paragraphs: {num_paragraphs}")

enumerated_paragraphs_list = enumerate_paragraphs(doc)


print("\nParagraph tuples:")
for item in enumerated_paragraphs_list:
    print(item)

# Output:
"""powershell
(0, 'This is the first paragraph of text that is being added to the document.')
(1, '')
(2, '')
(3, 'This is the second paragraph of text that is being added to the document.')
"""

print("\nParagraph numbers and text:")
for item in enumerated_paragraphs_list:
    print(item[0], item[1])

# Output:
"""powershell
0 This is the first paragraph of text that is being added to the document.
1
2
3 This is the second paragraph of text that is being added to the document.
"""
