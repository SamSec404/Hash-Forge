import json
import os

INTEGRITY_FILE = "models/integrity.json"

def load_integrity():
    if not os.path.exists(INTEGRITY_FILE):
        return {}

    with open(INTEGRITY_FILE, "r") as file:
        return json.load(file)


def save_integrity(data):
    with open(INTEGRITY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def register_file(filename, file_hash):
    data = load_integrity()
    data[filename] = file_hash
    save_integrity(data)


def verify_file(filename, new_hash):
    data = load_integrity()

    if filename not in data:
        return "NOT REGISTERED"

    if data[filename] == new_hash:
        return "VERIFIED"

    return "MODIFIED"




