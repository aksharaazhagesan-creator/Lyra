import subprocess

from speech import speak
from utils.file_search import find_file


def open_file(filename):

    matches = find_file(filename)

    # No matches
    if len(matches) == 0:
        speak(f"I couldn't find {filename}.")
        return

    # One match
    if len(matches) == 1:
        speak(f"Opening {filename}.")
        subprocess.run(["open", matches[0]])
        return

    # Multiple matches
    speak(f"I found {len(matches)} files named {filename}.")

    for i, file in enumerate(matches, start=1):
        print(f"{i}. {file}")

    speak("Please choose one.")