import argparse
import os

# Welcome Message
print("Welcome to TXT File Manager")

# Parser
parser = argparse.ArgumentParser(
    prog='.TXT File Manager',
    description='Used to create, update, and delete txt files'
)

parser.add_argument('filename')
parser.add_argument('data', nargs='?', default=None, help='Text data to be written to the file (optional)')
parser.add_argument('--delete', action='store_true', help='Delete the specified file')

# Update all the arguments
args = parser.parse_args()

# Variables
fileName = args.filename
data = args.data

# Delete functionality
if args.delete:
    try:
        os.remove(fileName)
        print(f"The file '{fileName}' has been deleted.")
    except FileNotFoundError:
        print(f"The file '{fileName}' does not exist.")
else:
    # Write or update the file
    if data is not None:
        with open(fileName, "a") as f:
            f.write(data)

    # Read and print the file content
    with open(fileName, "r") as f:
        print(f"The text in the file is '{f.read()}'\n")
