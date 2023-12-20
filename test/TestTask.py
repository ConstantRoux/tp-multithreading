import unittest
from copy import deepcopy

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

    def test_json(self):
        # test to test the serialization/deserialization
        task = Task(1, 100)
        task.work()

        # serialize the task
        task_json = task.to_json()

        # deserialize task
        task_after_json = Task.from_json(task_json)

        # check if it still the same object
        self.assertEqual(task, task_after_json)

    def test_task_eq(self):
        # Test class comparison
        # test object instantiation
        task1 = Task(identifier=1, size=100)
        list1 = []
        self.assertNotEqual(task1, list1)

        # test object with different id
        task2 = Task(identifier=2, size=100)
        self.assertNotEqual(task1, task2)

        # test object with different size
        task3 = Task(identifier=1, size=10)
        self.assertNotEqual(task1, task3)

        # test object with different id and different size
        task4 = Task(identifier=3, size=1000)
        self.assertNotEqual(task1, task4)

        # test object with same id and same size but with different A, b, X
        task5 = Task(identifier=1, size=100)
        self.assertNotEqual(task1, task5)

        # test object with itself
        self.assertEqual(task1, task1)

        # test object with copy of itself
        self.assertEqual(task1, deepcopy(task1))

        # test object with a copy of it and a simple modification on A
        task6 = deepcopy(task1)
        task6.A[0, 0] = task1.A[0, 0] + 1
        self.assertNotEqual(task1, task6)

        # test object with a copy of it and a simple modification on b
        task7 = deepcopy(task1)
        task7.b[0] = task7.b[0] + 1
        self.assertNotEqual(task1, task7)

        # test object with a copy of it and a simple modification on X
        task8 = deepcopy(task1)

        task8.X[0] = task8.X[0] + 1
        self.assertNotEqual(task1, task8)


if __name__ == "__main__":
    unittest.main()
