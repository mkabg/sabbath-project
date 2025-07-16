import json
import os

def save_to_file(lst, filename="data/shabbat_checklist.txt"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(lst, f, ensure_ascii=False, indent=2)

def load_from_file(filename="data/shabbat_checklist.txt"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return None
