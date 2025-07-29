import os, shutil
from pathlib import Path

# Walk through a folder tree and search for files with a certain extension (such as .pdf).
# Copy these files from their current location to a new folder
def selectively_copy(source, destination, extension):
    source = Path(source)
    destination = Path(destination)
    assert source.exists(), 'Invalid source'
    if not destination.exists():
        destination.mkdir()

    extension_len = len(extension)
    for folder_name, subfolders, filenames in os.walk(source):
        p = Path(folder_name)
        for filename in filenames:
            if len(filename) >= extension_len and filename[-extension_len:] == extension:
                shutil.copy(p / filename, destination)

