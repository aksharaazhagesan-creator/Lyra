import subprocess

from speech import speak
from utils.config_loader import load_config


folders = load_config("folders.json")


def open_folder(folder_name):
    folder_name = folder_name.lower()
    if folder_name not in folders:
        speak(f"Sorry, I couldn't find {folder_name}.")
        return

    speak(f"Opening {folder_name}.")

    subprocess.Popen([
        "open",
        folders[folder_name]
    ])