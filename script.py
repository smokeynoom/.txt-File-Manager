import argparse
import os

# Welcome Message
print("Welcome to TXT File Manager")

# Parser
parser = argparse.ArgumentParser(
    prog='.TXT File Manager',
    description='Used to create, update, and delete txt files'
)

parser.add_argument('filename', help='Name of the text file')
parser.add_argument('data', nargs='?', default=None, help='Text data to be written to the file (optional)')
parser.add_argument('--delete', action='store_true', help='Delete the specified file')
parser.add_argument('--rename', help='New name for the file')

# Update all the arguments
args = parser.parse_args()

# Variables
file_name = args.filename
data = args.data
new_name = args.rename

# Delete functionality
if args.delete:
    try:
        os.remove(file_name)
        print(f"The file '{file_name}' has been deleted.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
else:
    # Write or update the file
    if data is not None:
        with open(file_name, "a") as f:
            f.write(data)

    # Read and print the file content
    with open(file_name, "r") as f:
        file_content = f.read()
        if file_content:
            print(f"The text in the file '{file_name}' is: '{file_content}'\n")
        else:
            print(f"The file '{file_name}' is empty.\n")

# Rename Functionality
if new_name:
    try:
        os.rename(file_name, new_name)
        print(f"The file '{file_name}' has been renamed to '{new_name}'.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' does not exist.")
    except FileExistsError:
        print(f"Error: A file with the name '{new_name}' already exists.")
