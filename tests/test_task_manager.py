
import unittest
import tempfile
import json
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

import storage
import task_manager
from storage import StorageError


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = Path(self.temp_dir.name) / "tasks.json"

        self.patcher = patch.object(
            storage,
            "FILE_NAME",
            self.test_file
        )
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.temp_dir.cleanup()

    def capture_output(self, function, *args):
        output = StringIO()

        with redirect_stdout(output):
            function(*args)

        return output.getvalue()

    def test_add_task(self):
        task_manager.add_task("Learn Python")

        tasks = storage.load_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["id"], 1)
        self.assertEqual(tasks[0]["description"], "Learn Python")
        self.assertEqual(tasks[0]["status"], "todo")

    def test_empty_task(self):
        self.capture_output(task_manager.add_task, "   ")

        self.assertEqual(storage.load_tasks(), [])

    def test_update_task(self):
        task_manager.add_task("Learn Python")
        task_manager.update_task(1, "Learn Advanced Python")

        tasks = storage.load_tasks()

        self.assertEqual(
            tasks[0]["description"],
            "Learn Advanced Python"
        )

    def test_empty_update(self):
        task_manager.add_task("Learn Python")

        self.capture_output(task_manager.update_task, 1, " ")

        tasks = storage.load_tasks()
        self.assertEqual(tasks[0]["description"], "Learn Python")

    def test_delete_task(self):
        task_manager.add_task("Learn Python")
        task_manager.delete_task(1)

        self.assertEqual(storage.load_tasks(), [])

    def test_change_status(self):
        task_manager.add_task("Learn Python")
        task_manager.change_status(1, "done")

        tasks = storage.load_tasks()
        self.assertEqual(tasks[0]["status"], "done")

    def test_invalid_status(self):
        task_manager.add_task("Learn Python")

        self.capture_output(
            task_manager.change_status, 1, "invalid"
        )

        tasks = storage.load_tasks()
        self.assertEqual(tasks[0]["status"], "todo")

    def test_list_filter(self):
        task_manager.add_task("Task One")
        task_manager.add_task("Task Two")
        task_manager.change_status(2, "done")

        output = self.capture_output(
            task_manager.list_tasks, "done"
        )

        self.assertIn("Task Two", output)
        self.assertNotIn("Task One", output)

    def test_missing_file(self):
        self.assertEqual(storage.load_tasks(), [])
        self.assertTrue(self.test_file.exists())

    def test_invalid_json(self):
        self.test_file.write_text("{invalid json", encoding="utf-8")

        with self.assertRaises(StorageError):
            storage.load_tasks()

    def test_corrupted_structure(self):
        self.test_file.write_text(
            '{"not": "a list"}',
            encoding="utf-8"
        )

        with self.assertRaises(StorageError):
            storage.load_tasks()


if __name__ == "__main__":
    unittest.main()
