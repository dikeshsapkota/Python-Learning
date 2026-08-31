# File handling lets a program save information and read it back later.
# The "with open(...)" pattern automatically closes the file after use.

from tempfile import TemporaryDirectory
from pathlib import Path


with TemporaryDirectory() as folder:
    file_path = Path(folder) / "learning_note.txt"

    with open(file_path, "w") as note_file:
        note_file.write("Python can create and update files.\n")
        note_file.write("File handling is useful for logs, notes, and stored data.\n")

    with open(file_path, "r") as note_file:
        saved_note = note_file.read()

print("Saved file content:")
print(saved_note)
