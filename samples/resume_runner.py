# samples\resume_runner.py

import resume_heading as rh
import resume_address as ra

# Specify the file path for the .docx file:
file_path = "samples/output/ResumeRunner.docx"

doc = rh.add(file_path)
doc = ra.add(file_path, doc)
