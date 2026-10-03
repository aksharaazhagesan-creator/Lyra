import os
from utils.config_loader import load_config


projects = load_config("projects.json")
folders = load_config("folders.json")

SEARCH_PATHS = list(projects.values()) + list(folders.values())


def find_file(filename):

    matches = []

    for path in SEARCH_PATHS:

        for root, dirs, files in os.walk(path):

            for file in files:

                if file.lower() == filename.lower():

                    full_path = os.path.join(root, file)
                    matches.append(full_path)

    matches = list(set(matches))

    return matches

#os walk-->intreracts with the os and just asks if it can find the file in the paths that are defined in the projects and folders json files. It will return a list of all the matches it finds.
#subprocess is used-->used to open the file in the default application for that file type. It will open the first match it finds.
#usually used to open the process after finding it  