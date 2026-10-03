import subprocess

from speech import speak
from utils.config_loader import load_config


apps = load_config("apps.json")
projects = load_config("projects.json")


def open_project(project_name):

    project_name = project_name.lower()

    if project_name not in projects:
        speak(f"Sorry, I couldn't find {project_name}.")
        return

    speak(f"Opening {project_name} in Visual Studio Code.")

    subprocess.Popen([
        "open",
        "-a",
        apps["vscode"],
        projects[project_name]
    ])