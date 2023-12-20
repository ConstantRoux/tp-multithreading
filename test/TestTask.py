import unittest

import numpy as np

from src.Task import Task


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        # Test creating a Task instance
        task = Task(identifier=1, size=100)
        self.assertEqual(task.identifier, 1)
        self.assertEqual(task.size, 100)
        self.assertIsNone(task.execution_time)
        self.assertEqual(task.X.shape[0], task.size)
        self.assertEqual(task.b.shape[0], task.size)
        self.assertEqual(task.A.shape[0], task.size)
        self.assertEqual(task.A.shape[1], task.size)

    def test_task_work(self):
        # Test the work method of Task
        task = Task(identifier=1, size=100)
        task.work()
        self.assertEqual(task.X.shape[0], task.size)
        self.assertLessEqual(np.linalg.norm(task.A @ task.X - task.b), 1e-7)
        self.assertIsNotNone(task.execution_time)

    def test_task_eq(self):
        # Test class comparison
        task1 = Task(identifier=1, size=100)
        list1 = []
        self.assertNotEqual(task1, list1)

        task2 = Task(identifier=2, size=100)
        self.assertNotEqual(task1, task2)

        task3 = Task(identifier=1, size=10)
        self.assertNotEqual(task1, task3)

        task4 = Task(identifier=3, size=1000)
        self.assertNotEqual(task1, task4)

        task5 = Task(identifier=1, size=100)
        self.assertEqual(task1, task5)


if __name__ == "__main__":
    unittest.main()
