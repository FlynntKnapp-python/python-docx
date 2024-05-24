# samples\margin_set.py

from base import docx_builder

# Specify the file path for the .docx file:
file_path = "samples/output/MarginSet.docx"

# Load the Document:
doc = docx_builder.manage_docx_file(file_path, "load_or_create")

# Margin conversion:
# 1 inch = 914400 twips
conversion_factor = 914400  # twips per inch

# Get the first section of the document:
section = doc.sections[0]

# Define the margins in inches:
margin_top = 0.50
margin_bottom = 0.50
margin_left = 0.50
margin_right = 0.50

# Print the current margins:
print("Current Margins:")
print(
    "Top Margin:",
    section.top_margin,
    "twips",
    section.top_margin / conversion_factor,
    "inch(es)",
)
print(
    "Bottom Margin:",
    section.bottom_margin,
    "twips",
    section.bottom_margin / conversion_factor,
    "inch(es)",
)
print(
    "Left Margin:",
    section.left_margin,
    "twips",
    section.left_margin / conversion_factor,
    "inch(es)",
)
print(
    "Right Margin:",
    section.right_margin,
    "twips",
    section.right_margin / conversion_factor,
    "inch(es)",
)

# Set margins to 0.5 inches:
# doc = docx_builder.set_margins(doc, 0.75, 0.75, 0.75, 0.75)
doc = docx_builder.set_margins(
    doc, margin_top, margin_bottom, margin_left, margin_right
)

# Get the first section of the document:
section = doc.sections[0]

# Print the updated margins:
print("Updated Margins:")
print("Top Margin:", section.top_margin)
print("Bottom Margin:", section.bottom_margin)
print("Left Margin:", section.left_margin)
print("Right Margin:", section.right_margin)

# Save the document to a .docx file:
saved = docx_builder.manage_docx_file(file_path, doc, "save")
print("Saved: ", saved)
