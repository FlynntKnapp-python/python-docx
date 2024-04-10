# samples\margin_read.py

import os

from base import docx_builder

# Specify the file path for the .docx file:
file_path = os.getenv("MARGIN_READ_FILE")

# Load the Document:
doc = docx_builder.manage_docx_file(file_path, "load_or_create")

# Get the first section of the document:
section = doc.sections[0]

conversion_factor = 914400

# Print the margins:
print(
    f"Top Margin: "
    f"{section.top_margin} Units, "
    f"{section.top_margin / conversion_factor} Inches"
)
print(
    f"Bottom Margin: "
    f"{section.bottom_margin} Units, "
    f"{section.bottom_margin / conversion_factor} Inches"
)
print(
    f"Left Margin: "
    f"{section.left_margin} Units, "
    f"{section.left_margin / conversion_factor} Inches"
)
print(
    f"Right Margin: "
    f"{section.right_margin} Units, "
    f"{section.right_margin / conversion_factor} Inches"
)

"""
914400 / 1.0 = 914400 Units/Inch

0.5 Inches - 457200
0.75 Inches - 685800
1.0 Inches - 914400
1.25 Inches - 1143000
1.5 Inches - 1371600
"""
