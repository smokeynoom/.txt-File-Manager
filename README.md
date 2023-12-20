# .TXT FILE MANAGER

## Functionality
It can be used to create, update, and delete txt files.

## Three ways to use the file manager:-

### 1. Run the script with the --delete option to delete a file:
python script.py --delete filename.txt

### 2. Or run it without --delete to create or update a file:
python script.py filename.txt "New data to be added"

### For multiple lines, run:
python script.py filename.txt """Multiple
lines
to
be
added"""

### 3. Or run it --rename to rename a file
python script.py filename.txt --rename newFileName.txt