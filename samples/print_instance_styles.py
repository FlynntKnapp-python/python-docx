# samples\print_instance_styles.py

import utils
from docx import Document

# Create a new (empty) Document:
doc = Document()

# List the styles of the Document object:
attrs = utils.list_styles(doc)

# Output:
"""powershell
The document contains 164 styles:
Normal
Header
Header Char
Footer
Footer Char
Heading 1
Heading 2
Heading 3
Heading 4
Heading 5
Heading 6
Heading 7
Heading 8
Heading 9
Default Paragraph Font
Normal Table
No List
No Spacing
Heading 1 Char
Heading 2 Char
Heading 3 Char
Title
Title Char
Subtitle
Subtitle Char
List Paragraph
Body Text
Body Text Char
Body Text 2
Body Text 2 Char
Body Text 3
Body Text 3 Char
List
List 2
List 3
List Bullet
List Bullet 2
List Bullet 3
List Number
List Number 2
List Number 3
List Continue
List Continue 2
List Continue 3
macro
Macro Text Char
Quote
Quote Char
Heading 4 Char
Heading 5 Char
Heading 6 Char
Heading 7 Char
Heading 8 Char
Heading 9 Char
Caption
Strong
Emphasis
Intense Quote
Intense Quote Char
Subtle Emphasis
Intense Emphasis
Subtle Reference
Intense Reference
Book Title
TOC Heading
Table Grid
Light Shading
Light Shading Accent 1
Light Shading Accent 2
Light Shading Accent 3
Light Shading Accent 4
Light Shading Accent 5
Light Shading Accent 6
Light List
Light List Accent 1
Light List Accent 2
Light List Accent 3
Light List Accent 4
Light List Accent 5
Light List Accent 6
Light Grid
Light Grid Accent 1
Light Grid Accent 2
Light Grid Accent 3
Light Grid Accent 4
Light Grid Accent 5
Light Grid Accent 6
Medium Shading 1
Medium Shading 1 Accent 1
Medium Shading 1 Accent 2
Medium Shading 1 Accent 3
Medium Shading 1 Accent 4
Medium Shading 1 Accent 5
Medium Shading 1 Accent 6
Medium Shading 2
Medium Shading 2 Accent 1
Medium Shading 2 Accent 2
Medium Shading 2 Accent 3
Medium Shading 2 Accent 4
Medium Shading 2 Accent 5
Medium Shading 2 Accent 6
Medium List 1
Medium List 1 Accent 1
Medium List 1 Accent 2
Medium List 1 Accent 3
Medium List 1 Accent 4
Medium List 1 Accent 5
Medium List 1 Accent 6
Medium List 2
Medium List 2 Accent 1
Medium List 2 Accent 2
Medium List 2 Accent 3
Medium List 2 Accent 4
Medium List 2 Accent 5
Medium List 2 Accent 6
Medium Grid 1
Medium Grid 1 Accent 1
Medium Grid 1 Accent 2
Medium Grid 1 Accent 3
Medium Grid 1 Accent 4
Medium Grid 1 Accent 5
Medium Grid 1 Accent 6
Medium Grid 2
Medium Grid 2 Accent 1
Medium Grid 2 Accent 2
Medium Grid 2 Accent 3
Medium Grid 2 Accent 4
Medium Grid 2 Accent 5
Medium Grid 2 Accent 6
Medium Grid 3
Medium Grid 3 Accent 1
Medium Grid 3 Accent 2
Medium Grid 3 Accent 3
Medium Grid 3 Accent 4
Medium Grid 3 Accent 5
Medium Grid 3 Accent 6
Dark List
Dark List Accent 1
Dark List Accent 2
Dark List Accent 3
Dark List Accent 4
Dark List Accent 5
Dark List Accent 6
Colorful Shading
Colorful Shading Accent 1
Colorful Shading Accent 2
Colorful Shading Accent 3
Colorful Shading Accent 4
Colorful Shading Accent 5
Colorful Shading Accent 6
Colorful List
Colorful List Accent 1
Colorful List Accent 2
Colorful List Accent 3
Colorful List Accent 4
Colorful List Accent 5
Colorful List Accent 6
Colorful Grid
Colorful Grid Accent 1
Colorful Grid Accent 2
Colorful Grid Accent 3
Colorful Grid Accent 4
Colorful Grid Accent 5
Colorful Grid Accent 6
"""
