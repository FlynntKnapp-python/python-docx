# `python-docx` Example - ChatGPT

## [`python-docx` Example - ChatGPT](https://chat.openai.com/share/a0e868bf-5eed-4ffe-a368-7f8d0b3fec1e)

You can use the `python-docx` library to create and manipulate Microsoft Word (.docx) files in Python. It provides a rich set of features that allow you to create documents, add text, images, tables, and more.

Here's a simple example of how to use `python-docx` to create a Word document with a title, a paragraph of text, and then save it as a `.docx` file:

1. First, you need to install the `python-docx` library if you haven't already. You can install it using pip:

```sh
pip install python-docx
```

2. Then, you can use the following Python code to create a new Word document:

```python
from docx import Document

# Create a new Document
doc = Document()

# Add a title to the document
doc.add_heading('Document Title', 0)

# Add a paragraph of text
p = doc.add_paragraph('This is a simple paragraph that is being added to the document. ')

# Save the document to a .docx file
doc.save('example.docx')
```

This code creates a new Word document, adds a title with the text "Document Title" at the top of the document, adds a paragraph with some sample text, and then saves the document as `example.docx` in the current working directory.

You can add more content to the document by using methods like `add_paragraph()` for additional paragraphs, `add_heading()` for headings at different levels, and many other methods provided by `python-docx` to include tables, images, and other document elements.

