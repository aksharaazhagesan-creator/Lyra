from commands.hello import hello
from commands.time import tell_time
from commands.date import tell_date
from commands.launcher import open_application
from commands.project_manager import open_project
from commands.folder_manager import open_folder
from commands.file_manager import open_file


def execute(tool, arguments):

    if tool == "hello":
        hello()
        return

    if tool == "tell_time":
        tell_time()
        return

    if tool == "tell_date":
        tell_date()
        return

    if tool == "open_application":
        open_application(arguments["application"])
        return

    if tool == "open_project":
        open_project(arguments["project"])
        return

    if tool == "open_folder":
        open_folder(arguments["folder"])
        return

    if tool == "open_file":
        open_file(arguments["filename"])
        return

    print("Unknown tool:", tool)