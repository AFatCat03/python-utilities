import pyperclip, time
from pathlib import Path

# Adapted from "A cross-platform clipboard monitoring and recording tool" by Al Sweigart
# Modifications: Saves clipboard content to a file (recorder.txt) on the Desktop instead of printing
def clipboard_recorder():
    print('Recording clipboard... (Ctrl-C to stop)')
    previous_content = ''
    try:
        output_file = open(Path.home() / 'Desktop/recorder.txt', 'w', encoding='UTF-8')
        while True:
            content = pyperclip.paste() # Get clipboard contents.

            if content != previous_content:
                # If it's different from the previous, write it:
                output_file.write(content + '\n')
                previous_content = content

            time.sleep(0.01) # Pause to avoid hogging the CPU.
    except KeyboardInterrupt:
        output_file.close()
