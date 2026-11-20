
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

import task_manager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = Path(self.temp_dir.name) / "tasks.json"

        self.file_patcher = patch.object(
            task_manager,
            "load_tasks",
            side_effect=self.load_tasks
        )
        self.save_patcher = patch.object(
            task_manager,
            "save_tasks",
            side_effect=self.save_tasks
        )

        self.file_patcher.start()
        self.save_patcher.start()

    def tearDown(self):
        self.file_patcher.stop()
        self.save_patcher.stop()
        self.temp_dir.cleanup()

    def load_tasks(self):
        import json
        if not self.test_file.exists():
            return []
        with open(self.test_file, "r") as file:
            return json.load(file)

    def save_tasks(self, tasks):
        import json
        with open(self.test_file, "w") as file:
            json.dump(tasks, file)

    def test_add_task(self):
        task_manager.add_task("Learn Python")
        tasks = self.load_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Learn Python")
        self.assertEqual(tasks[0]["status"], "todo")

    def test_empty_task(self):
        task_manager.add_task("   ")
        self.assertEqual(self.load_tasks(), [])

    def test_update_task(self):
        task_manager.add_task("Learn Python")
        task_manager.update_task(1, "Learn Advanced Python")

        tasks = self.load_tasks()
        self.assertEqual(
            tasks[0]["description"],
            "Learn Advanced Python"
        )

    def test_delete_task(self):
        task_manager.add_task("Learn Python")
        task_manager.delete_task(1)

        self.assertEqual(self.load_tasks(), [])

    def test_change_status(self):
        task_manager.add_task("Learn Python")
        task_manager.change_status(1, "done")

        tasks = self.load_tasks()
        self.assertEqual(tasks[0]["status"], "done")


if __name__ == "__main__":
    unittest.main()
