# ✦ Automating File Renaming and Content Update After Name Change (Bash and Python)
*In accordance with company records, Jane Pitt has officially changed her last name to Jane Doe. Although her system username (jpitt) was already updated to jdoe, some files still contain references to her previous name - either in file names, or within the contents of documents and tables. To keep personnel records consistent and up to date, we are tasked with automating the process of locating all files associated with Jane Pitt and making the appropriate updates to reflect her new last name.*
---
## 📌 Objective:
* Practice using the cat, grep, and cut commands for file operations.
* Use > and >> commands to redirect I/O stream.
* Replace a substring using Python.
* Run bash commands in Python.
---
### 📦 Installing dependencies:
```bash
pip install -r requirements.txt
```
### 🗂️ Data Generation
#### ➤ Create directories : 
* `data` - for storing data files;
* `scripts` - for storing script files
```bash
mkdir data scripts
```
#### ➤ Create the `generate_file_csv.sh` script to add data to the file `jpitt_contact_07292018.csv`.
```bash
nano scripts/generate_file_csv.sh
```
#### ➤ Add data to the file `generate_file_csv.sh`
```bash
#!/bin/bash
file_path=data/jpitt_contact_07292018.csv
echo "Full Name,Position,Department" > $file_path
echo "Audrey Miller,Product Manager,Development" >> $file_path
echo "Jane Pitt,QA Engineer,QA" >> $file_path
echo "Bailey Thomas,Head HR,Human Resources" >> $file_path
```
#### ➤ Make the file `generate_file_csv.sh` executable:
```bash
chmod +x scripts/generate_file_csv.sh
```
#### ➤ Run the `generate_file_csv.sh` bash script . This will generate a new file named `jpitt_contact_07292018.csv`
```bash
./scripts/generate_file_csv.sh
```
#### ➤ Create the `generate_file_docx.sh` script to add data to the file `jpitt_profile_07272018.docx`.
```bash
nano scripts/generate_file_docx.py
```
#### ➤ Add data to the file `generate_file_docx.py`
```python
#!/usr/bin/env python3

from docx import Document

# Create a new document
doc = Document()

# Add a title
doc.add_heading('Employee Profile', level=1)

# Add a regular paragraph
doc.add_paragraph('This document contains a description of the employee.')

# Add a table with data
data = [
    ['Name', 'Position', 'Department', 'Start Day', 'End Day'],
    ['Jane Pitt', 'Junior QA', 'IT', '22-03-2023', '12-03-2024'],
    ['Jane Pitt', 'Middle QA', 'IT', '22-03-2023'],
]

# Create a table with headings
table = doc.add_table(rows=1, cols=len(data[0]))
table.style = 'Table Grid'
hdr_cells = table.rows[0].cells

# Fill in the table headings
for i, heading in enumerate(data[0]):
    hdr_cells[i].text = heading

# Add data rows
for row_data in data[1:]:
    row = table.add_row().cells
    for i in range(len(data[0])):
        if i < len(row_data):
            row[i].text = row_data[i]
        else:
            row[i].text = ''

# Save the document
doc.save('./data/jpitt_profile_07272018.docx')
```
#### ➤ Make the file `generate_file_docx.py` executable:
```bash
chmod +x scripts/generate_file_docx.py
```
#### ➤ Run the `generate_file_docx.py` bash script. This will generate a new file named `jpitt_profile_07272018.docx`
```bash
./scripts/generate_file_docx.py
```
---
### 🔍 Filtering and Recording Files Matching a Specific Name
#### ➤ To view files in data directory, use the following command:
```bash
ls data
```
#### ➤ To view the contents of the `list.txt` file, use the following command:
```bash
cat list.txt
```
#### ➤ Create a new file named `find_jpitt.sh`.
```bash
nano ./scripts/find_jpitt.sh
```
#### ➤ A script `find_jpitt.sh` within the scripts directory that captures all Jane lines and stores them in a separate text file called `old_files.txt`.
```bash
#!/bin/bash

# Reset the file. If the file does not yet exist, it will be created as empty; if it exists, it will be cleared.
# > - redirect output to a file (nothing is displayed, but the file is reset).
> data/old_files.txt

# grep: search for lines containing the word "jpitt" in the file list.txt.
# -w: search for the whole word, not just part of it.
#|: Transferring the grep search result to while.
# while: processes each line found line by line.
# read: reads data from somewhere and writes this data to the variable line:
# # from the user (keyboard input),
# # from another command (via |) - this situation,
# # from the file.
grep -w 'jpitt' list.txt | while read -r line; do
  
   # echo "$line": outputs the value of the variable line.
   # |: passes this line to the next command - awk.
   # awk: splits a string into fields based on spaces.
   # $3: the third word.
   filepath=$(echo "$line" | awk '{print $3}')

   # Creates the full path to the file by adding the beginning to the extracted path.
   cleanpath="${filepath#/}" # ${filepath#pattern}: Special Bash syntax for deleting part of a string.
   realpath="$(pwd)/data/${cleanpath}"

   # -e: checks whether a file or directory exists.
   if [ -e "$realpath" ]; then
     
       # If the file exists, its path is added to the old_files.txt file.
       echo "$realpath" >> data/old_files.txt
   fi
done
```
#### ➤ Make the file executable:
```bash
chmod +x scripts/find_jpitt.sh
```
#### ➤ Run the bash script `find_jpitt.sh`. This will generate a new file named `old_files.txt`, which consists of all the files containing the name jpitt
```bash
./scripts/find_jpitt.sh
```
#### ➤ View the contents of the newly generated file.
```bash
cat old_files.txt
```
---
### ✏️ Rename files using Python script
#### ➤ Create a new file named `change_jpitt.py`.
```bash
nano scripts/change_jpitt.py
```
#### ➤ Write a Python script `change_jpitt.py``
```python
#!/usr/bin/env python3
import sys # Allows obtaining parameters passed when the script is launched.
import subprocess

# sys.argv: a list of command line arguments that are passed when the script is run.
# sys.argv[0]: the name of the script is "change_jpitt.py`".
# sys.argv[1]: the first parameter is "old_files.txt".
with open(sys.argv[1], "r") as f:
    for line in f:
        old_name = line.strip()
        new_name = old_name.replace("jpitt", "jdoe")
        subprocess.run(["mv", old_name, new_name])
```
#### ➤ Make the file `change_jpitt.py` executable
```bash
chmod +x scripts/change_jpitt.py
```
#### ➤ Run the script and pass the file `old_files.txt` as a command line argument.
```bash
./scripts/change_jpitt.py data/old_files.txt
```
#### ➤ Navigate to the directory and use the ls command to view renamed files.
```bash
ls data
```
---
### ✏️ Updating data within documents
#### ➤ Create a new file named `update_name_and_dates_in_docx.py`.
```bash
nano scripts/update_name_and_dates_in_docx.py
```
#### ➤ Add data to the file `update_name_and_dates_in_docx.py`
```python
#!/usr/bin/env python3
from docx import Document
from datetime import datetime
import sys

# ✅ Check: if the script is run without a file, it will terminate.
# sys.argv: list of parameters from the command line.
# sys.argv[0]: the script itself.
# sys.argv[1]: path to the file (i.e. data/jdoe_profile.docx).
if len(sys.argv) < 2:
    sys.exit(1)

# Storing the path to the file in the file_path variable so that we can work with it later.
file_path = sys.argv[1]
# Open the Word file. Now doc is a Word document object that we can work with (read and change).
doc = Document(file_path)

# Get the current date in DD-MM-YYYY format.
today = datetime.today().strftime("%d-%m-%Y")

# Go through all the tables.
for table in doc.tables:
    headers = [cell.text for cell in table.rows[0].cells]

    # Looking for the necessary indices.
    try:
        name_idx = headers.index("Name")
        start_idx = headers.index("Start Day")
        end_idx = headers.index("End Day")
    except ValueError:
        continue  # Skip the table if the structure does not match.

    # Find the last line with "Jane Pitt".
    last_pitt_row = None
    for row in table.rows[1:]:
        if "Jane Pitt" in row.cells[name_idx].text:
            last_pitt_row = row

    if last_pitt_row:
        # If the end date is blank, enter today's date.
        if last_pitt_row.cells[end_idx].text.strip() == "":
            last_pitt_row.cells[end_idx].text = today

        # Create a new line.
        new_row = table.add_row().cells
        for i, cell in enumerate(last_pitt_row.cells):
            new_row[i].text = cell.text

        # Update the name and start date.
        new_row[name_idx].text = "Jane Doe"
        new_row[start_idx].text = today
        new_row[end_idx].text = ""  # Clear the end date.

# Save changes.
doc.save(file_path)
```
#### ➤ Make the file `update_name_and_dates_in_docx.py` executable
```bash
chmod +x scripts/update_name_and_dates_in_docx.py
```
#### ➤ Run the script `update_name_and_dates_in_docx.py`.
```bash
./scripts/update_name_and_dates_in_docx.py data/jdoe_profile_07272018.docx
```
#### ➤ Create a new file named `replace_in_csv.py`.
```bash
nano scripts/replace_in_csv.py
```
#### ➤ Add data to the file `replace_in_csv.py`
```python
#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

content = content.replace("Jane Pitt", "Jane Doe")

with open(file_path, "w", encoding="utf-8") as file:
    file.write(content)
```
#### ➤ Make the file `replace_in_csv.py` executable
```bash
chmod +x scripts/replace_in_csv.py
```
#### ➤ Run the script `replace_in_csv.py`.
```bash
./scripts/replace_in_csv.py data/jdoe_contact_07292018.csv
```