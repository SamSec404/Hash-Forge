import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

HISTORY_FILE = os.path.join(
    BASE_DIR,
    "models",
    "history.json"
)


def load_history():

    if not os.path.exists(HISTORY_FILE):

        return []

    with open(HISTORY_FILE, "r") as file:

        return json.load(file)


def save_history(history):

    with open(HISTORY_FILE, "w") as file:

        json.dump(
            history,
            file,
            indent=4
        )


def add_history(entry):

    history = load_history()

    history.insert(0, entry)

    history = history[:20]

    save_history(history)
