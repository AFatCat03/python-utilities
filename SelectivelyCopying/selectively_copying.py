import os, sys, shutil
from pathlib import Path

# Walk through a folder tree and search for files with a certain extension (such as .pdf).
# Copy these files from their current location to a new folder
def selectively_copy(extension, source, destination):
    source = Path(source)
    destination = Path(destination)
    assert source.exists(), 'Invalid source'
    if not destination.exists():
        destination.mkdir()

    extension_len = len(extension)
    for folder_name, subfolders, filenames in os.walk(source):
        if Path(folder_name).resolve() == destination.resolve():
            continue
        p = Path(folder_name)
        for filename in filenames:
            if len(filename) >= extension_len and filename[-extension_len:] == extension:
                print(f'{folder_name}\{filename}')
                file_path = p / f'{filename}'
                output_path = destination / f'{filename[:-extension_len]}#1{extension}'
                while os.path.exists(output_path):
                    output_path = str(output_path)
                    # print(output_path[output_path.rfind('#') + 1: output_path.rfind('.')])
                    output_path = Path(f"{output_path[:output_path.rfind('#') + 1]}{int(output_path[output_path.rfind('#') + 1: output_path.rfind('.')]) + 1}{output_path[output_path.rfind('.'):]}")
                shutil.copy(file_path, output_path)


extension = sys.argv[1] if len(sys.argv) > 1 else '.png'
source = Path(sys.argv[2] if len(sys.argv) > 2 else 'D:/Latex')
destination = Path(sys.argv[3] if len(sys.argv) > 3 else source / f'{extension[1:]}_folder')

selectively_copy(extension, source, destination)
