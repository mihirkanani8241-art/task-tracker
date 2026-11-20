
# Task Tracker CLI

A simple command-line task management application built using Python.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in-progress
- Mark tasks as done
- List all tasks
- Filter tasks by status
- Persistent JSON storage
- Input validation and error handling
- Automated unit tests

## Requirements

- Python 3.10 or newer
- Git (optional)

No external Python libraries are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/mihirkanani8241-art/task-tracker.git
```

Open the project directory:

```bash
cd task-tracker
```

## Usage

Add a task:

```bash
python main.py add "Learn Python"
```

List all tasks:

```bash
python main.py list
```

Update a task:

```bash
python main.py update 1 "Learn Advanced Python"
```

Delete a task:

```bash
python main.py delete 1
```

Mark as in progress:

```bash
python main.py mark-in-progress 1
```

Mark as done:

```bash
python main.py mark-done 1
```

Filter by status:

```bash
python main.py list todo
python main.py list in-progress
python main.py list done
```

View help:

```bash
python main.py help
```

## Task Structure

Each task contains:

- id: Unique task identifier
- description: Task description
- status: todo, in-progress, or done
- createdAt: Creation timestamp
- updatedAt: Last modification timestamp

## Data Storage

Tasks are stored in `tasks.json`.

The application creates the JSON file automatically if it does not exist.

## Testing

Run automated tests:

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
task-tracker/
├── main.py
├── task_manager.py
├── storage.py
├── tasks.json
├── README.md
├── .gitignore
└── tests/
    └── test_task_manager.py
```

## Technologies

- Python
- JSON
- Git
- GitHub
- unittest

## Author

Mihir Kanani
