# samples\paragraph_space_set.py

from base import docx_builder

# Specify the file path for the .docx file:
file_path = "samples/output/ParagraphSpaceSet.docx"

# Load the Document:
doc = docx_builder.manage_docx_file(file_path, "delete_and_create")

space_before_p1 = 0
space_after_p1 = 0

# Add a paragraph with a specific space before and after:
p1 = doc.add_paragraph(
    f"This is the first paragraph: "
    f"Space before: {space_before_p1}, "
    f"Space after: {space_after_p1}."
)
# Adjust spacing of p1:
p1.paragraph_format.space_before = space_before_p1
p1.paragraph_format.space_after = space_after_p1

space_before_p2 = 0
space_after_p2 = 228600

p2 = doc.add_paragraph(
    f"This is the second paragraph: "
    f"Space before: {space_before_p2}, "
    f"Space after: {space_after_p2}."
)
# Adjust spacing of p2:
p2.paragraph_format.space_before = space_before_p2
p2.paragraph_format.space_after = space_after_p2

space_before_p3 = 228600
space_after_p3 = 228600

p3 = doc.add_paragraph(
    f"This is the third paragraph: "
    f"Space before: {space_before_p3}, "
    f"Space after: {space_after_p3}."
)
# Adjust spacing of p3:
p3.paragraph_format.space_before = space_before_p3
p3.paragraph_format.space_after = space_after_p3

space_before_p4 = 228600
space_after_p4 = 228600

p4 = doc.add_paragraph(
    f"This is the fourth paragraph: "
    f"Space before: {space_before_p4}, "
    f"Space after: {space_after_p4}."
)

# Adjust spacing of p4:
p4.paragraph_format.space_before = space_before_p4
p4.paragraph_format.space_after = space_after_p4

space_before_p5 = 457200
space_after_p5 = 0

p5 = doc.add_paragraph(
    f"This is the fifth paragraph: "
    f"Space before: {space_before_p5}, "
    f"Space after: {space_after_p5}."
)

# Adjust spacing of p5:
p5.paragraph_format.space_before = space_before_p5
p5.paragraph_format.space_after = space_after_p5

# Read the space before and after each paragraph:
print("Space Before p1:", p1.paragraph_format.space_before)
print("Space After p1:", p1.paragraph_format.space_after)
print("Space Before p2:", p2.paragraph_format.space_before)
print("Space After p2:", p2.paragraph_format.space_after)
print("Space Before p3:", p3.paragraph_format.space_before)
print("Space After p3:", p3.paragraph_format.space_after)
print("Space Before p4:", p4.paragraph_format.space_before)
print("Space After p4:", p4.paragraph_format.space_after)
print("Space Before p5:", p5.paragraph_format.space_before)
print("Space After p5:", p5.paragraph_format.space_after)


# Save the document to a .docx file:
saved = docx_builder.save_docx(file_path, doc)
print("Saved: ", saved)
