import os
from typing import List

import yaml

LOGGERS = "DeltaMusic"

languages = {}
languages_present = {}

def get_string(lang: str):
    return languages[lang]

def get_command(command_name):
    # Implementation of get_command function
    # For example, it could return a command string based on the command_name
    commands = {
        "speedtest": "speedtest",
        "spt": "spt"
    }
    return commands.get(command_name, "")

for filename in os.listdir(r"./strings/langs/"):
    if "en" not in languages:
        languages["en"] = yaml.safe_load(
            open(r"./strings/langs/en.yml", encoding="utf8")
        )
        languages_present["en"] = languages["en"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]
    try:
        languages_present[language_name] = languages[language_name]["name"]
    except:
        print("Ada masalah dengan file bahasa di dalam bot.")
        exit()
