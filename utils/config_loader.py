import json
def load_config(filename):
    with open(f"config/{filename}", "r") as file:
        return json.load(file)