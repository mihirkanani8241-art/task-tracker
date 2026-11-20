
import sys

from task_manager import (
    add_task,
    list_tasks,
    update_task,
    delete_task,
    change_status
)


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python main.py <command>")
        return

    command = args[0]

    try:
        if command == "add":
            add_task(" ".join(args[1:]))

        elif command == "list":
            status = args[1] if len(args) > 1 else None

            if status and status not in ["todo", "in-progress", "done"]:
                print("Error: Invalid status.")
                return

            list_tasks(status)

        elif command == "update":
            if len(args) < 3:
                print('Usage: python main.py update <id> "description"')
                return

            update_task(int(args[1]), " ".join(args[2:]))

        elif command == "delete":
            delete_task(int(args[1]))

        elif command in ["mark-in-progress", "mark-done"]:
            task_id = int(args[1])
            status = "in-progress" if command == "mark-in-progress" else "done"
            change_status(task_id, status)

        else:
            print(f"Unknown command: {command}")

    except (ValueError, IndexError):
        print("Error: Invalid or missing task ID.")


if __name__ == "__main__":
    main()
