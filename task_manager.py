
from datetime import datetime
from storage import load_tasks, save_tasks


VALID_STATUSES = ["todo", "in-progress", "done"]


def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def add_task(description):
    description = description.strip()

    if not description:
        print("Error: Task description cannot be empty.")
        return

    tasks = load_tasks()
    new_id = max((task["id"] for task in tasks), default=0) + 1

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": current_time(),
        "updatedAt": current_time()
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_id})")


def list_tasks(status=None):
    tasks = load_tasks()

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(
            f'ID: {task["id"]} | '
            f'{task["description"]} | '
            f'{task["status"]}'
        )


def update_task(task_id, description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            description = description.strip()

            if not description:
                print("Error: Description cannot be empty.")
                return

            task["description"] = description
            task["updatedAt"] = current_time()
            save_tasks(tasks)

            print(f"Task {task_id} updated successfully.")
            return

    print(f"Task with ID {task_id} not found.")


def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully.")
            return

    print(f"Task with ID {task_id} not found.")


def change_status(task_id, status):
    if status not in VALID_STATUSES:
        print("Error: Invalid status.")
        return

    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = current_time()
            save_tasks(tasks)

            print(f"Task {task_id} marked as {status}.")
            return

    print(f"Task with ID {task_id} not found.")
