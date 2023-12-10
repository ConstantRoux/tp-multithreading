import unittest

from src.Task import Task


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        # Test creating a Task instance
        task = Task(identifier=1, size=100)
        self.assertEqual(task.identifier, 1)
        self.assertEqual(task.size, 100)
        self.assertIsNone(task.execution_time)

    def test_task_work(self):
        # Test the work method of Task
        task = Task(identifier=1, size=100)
        task.work()
        self.assertIsNotNone(task.execution_time)


if __name__ == "__main__":
    unittest.main()
