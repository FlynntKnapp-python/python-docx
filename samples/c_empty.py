# samples\c_empty.py

from base.builder import DocxBuilder

# Specify the file path for the .docx file:
file_path = "samples/output/CEmpty.docx"

# Create a new DocxBuilder:
doc = DocxBuilder(file_path)

# Save the document to a .docx file:
saved = doc.save()
print(f"Document saved: {saved}")
