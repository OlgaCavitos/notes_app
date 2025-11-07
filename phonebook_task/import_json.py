import json

FILE="phonebook.json"

def upload_phonebook():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return{"contacts":[]}
    except json.JSONDecodeError:
        return{"contacts":[]}


def save_phonebook(data):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

