
import json
from pathlib import Path

FILE_NAME = Path(__file__).parent / "tasks.json"


class StorageError(Exception):
    """Raised when task storage cannot be read or written."""


def load_tasks():
    if not FILE_NAME.exists():
        save_tasks([])
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = json.load(file)

    except json.JSONDecodeError as error:
        raise StorageError(
            "tasks.json contains invalid JSON. "
            "Please repair or restore the file."
        ) from error

    except OSError as error:
        raise StorageError(
            f"Could not read tasks.json: {error}"
        ) from error

    if not isinstance(tasks, list):
        raise StorageError(
            "Invalid tasks.json format. Expected a list."
        )

    for task in tasks:
        if not isinstance(task, dict):
            raise StorageError("Invalid task data found.")

        required = {
            "id", "description", "status",
            "createdAt", "updatedAt"
        }

        if not required.issubset(task):
            raise StorageError("A task is missing required fields.")

    return tasks


def save_tasks(tasks):
    temp_file = FILE_NAME.with_suffix(".tmp")

    try:
        with open(temp_file, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)

        temp_file.replace(FILE_NAME)

    except OSError as error:
        raise StorageError(
            f"Could not save tasks: {error}"
        ) from error
