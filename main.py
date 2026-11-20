
import sys

from task_manager import (
    add_task,
    list_tasks,
    update_task,
    delete_task,
    change_status
)

from storage import StorageError


VALID_STATUSES = ("todo", "in-progress", "done")


def show_help():
    print("""
Task Tracker CLI

Commands:

  add <description>
      Add a new task.

  list
      List all tasks.

  list <status>
      Filter tasks by status.

  update <id> <description>
      Update a task description.

  delete <id>
      Delete a task.

  mark-in-progress <id>
      Mark a task as in progress.

  mark-done <id>
      Mark a task as completed.

  help
      Show this help message.

Available statuses: todo, in-progress, done
""")


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv

    if not args:
        show_help()
        return

    command = args[0]

    try:
        if command == "help":
            show_help()

        elif command == "add":
            if len(args) < 2:
                print('Usage: python main.py add "description"')
                return

            add_task(" ".join(args[1:]))

        elif command == "list":
            if len(args) > 2:
                print("Error: Too many arguments.")
                return

            status = args[1] if len(args) == 2 else None

            if status and status not in VALID_STATUSES:
                print("Error: Invalid status.")
                return

            list_tasks(status)

        elif command == "update":
            if len(args) < 3:
                print('Usage: python main.py update <id> "description"')
                return

            task_id = int(args[1])
            update_task(task_id, " ".join(args[2:]))

        elif command == "delete":
            if len(args) != 2:
                print("Usage: python main.py delete <id>")
                return

            task_id = int(args[1])
            delete_task(task_id)

        elif command in ("mark-in-progress", "mark-done"):
            if len(args) != 2:
                print(f"Usage: python main.py {command} <id>")
                return

            task_id = int(args[1])

            status = (
                "in-progress"
                if command == "mark-in-progress"
                else "done"
            )

            change_status(task_id, status)

        else:
            print(f"Unknown command: {command}")
            print("Run 'python main.py help' for available commands.")

    except ValueError:
        print("Error: Task ID must be a valid integer.")

    except StorageError as error:
        print(f"Storage error: {error}")

    except OSError as error:
        print(f"File operation error: {error}")


if __name__ == "__main__":
    main()
