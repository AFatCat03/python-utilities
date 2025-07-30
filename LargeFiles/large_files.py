import os
from pathlib import Path

# Walk through a folder tree and search for exceptionally large files
# Print these files with their absolute path to the screen
def large_files(folder, threshold = 100 * 1024 * 1024):
    folder = Path(folder)
    assert folder.exists(), 'Invalid folder'

    for folder_name, subfolders, filenames in os.walk(folder):
        p = Path(folder_name)
        for filename in filenames:
            path = p / filename
            if os.path.getsize(path) > threshold:
                print(path)

