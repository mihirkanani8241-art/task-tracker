
import json
from pathlib import Path

FILE_NAME = Path(__file__).parent / "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = json.load(file)
            return tasks if isinstance(tasks, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)