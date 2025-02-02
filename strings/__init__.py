import os
from typing import List

import yaml

LOGGERS = "DeltaMusic"

languages = {}
languages_present = {}

def get_string(lang: str):
    return languages[lang]

for filename in os.listdir(r"./strings/langs/"):
    if "id" not in languages:
        languages["id"] = yaml.safe_load(
            open(r"./strings/langs/id.yml", encoding="utf8")
        )
        languages_present["id"] = languages["id"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "id":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["id"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["id"][item]
        try:
            languages_present[language_name] = languages[language_name]["name"]
        except:
            print("Ada masalah dengan file bahasa di dalam bot.")
            exit()
    # Ensure 'en' language is loaded
    if "en" not in languages:
        languages["en"] = yaml.safe_load(
            open(r"./strings/langs/en.yml", encoding="utf8")
        )
        languages_present["en"] = languages["en"]["name"]
