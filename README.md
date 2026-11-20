# Task Tracker CLI

A simple command-line application built with Python to manage and track daily tasks.

## Features

- Add a new task
- List all tasks
- Filter tasks by status (`todo`, `in-progress`, `done`)
- Update task descriptions
- Delete tasks
- Mark tasks as in progress or done
- Store tasks in a JSON file
- Automatically track creation and update timestamps

## Requirements

- Python 3.8 or later

## Installation

Clone the repository:

```bash
git clone https://github.com/mihirkanani8241-art/task-tracker.git
cd task-tracker
```

## Usage

Add a task:

```bash
python main.py add "Study Python"
```

List all tasks:

```bash
python main.py list
```

Filter tasks:

```bash
python main.py list todo
python main.py list in-progress
python main.py list done
```

Update a task:

```bash
python main.py update 1 "Study Python daily"
```

Delete a task:

```bash
python main.py delete 1
```

Change task status:

```bash
python main.py mark-in-progress 1
python main.py mark-done 1
```

Show help:

```bash
python main.py help
```

## Running Tests

```bash
python -m unittest discover -s tests -v
```

## Project URL

https://roadmap.sh/projects/task-tracker

## Author

Mihir Kanani

GitHub: https://github.com/mihirkanani8241-art