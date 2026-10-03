import subprocess

from speech import speak
from utils.config_loader import load_config


apps = load_config("apps.json")


def open_application(app_name):

    if app_name not in apps:
        speak(f"Sorry, I couldn't find {app_name}.")
        return

    speak(f"Opening {app_name}.")

    subprocess.Popen([
        "open",
        apps[app_name]
    ])