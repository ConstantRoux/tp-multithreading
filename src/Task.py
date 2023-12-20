import logging
from time import perf_counter

import numpy as np


class Task:
    def __init__(self, identifier: int, size: int):
        """
        Initializes a task with a specified identifier and size.

        :param identifier: The identifier of the task.
        :param size: The size of vectors to generate for the linear system.
        """
        self.identifier = identifier
        self.size = size

        self.A = np.random.rand(self.size, self.size)
        self.X = np.zeros(self.size)
        self.b = np.random.rand(self.size)

        self.execution_time = None

    def work(self) -> float:
        """
        Performs the task by solving a linear system AX=B.

        Uses the generated random vectors A and b of the specified size, solves the linear system AX=b using numpy.linalg.solve,
        saves the solution in X, measures the execution time, and prints in DEBUG the solution.

        :return: The execution time of the task in seconds.
        """
        # solve linear system ax=b and measure start and stop time
        start_time = perf_counter()
        self.X = np.linalg.solve(self.A, self.b)
        end_time = perf_counter()

        # compute execution time
        self.execution_time = end_time - start_time

        # print the task id and the execution time in DEBUG logging level
        logging.debug(f"Task {self.identifier}: {self.execution_time:.2f} seconds")

        # return execution time
        return self.execution_time

    def __eq__(self, other: "Task") -> bool:
        """
        Compare the current Task class instantiation with the other object.

        :param other: The object to compare.
        :return: True if object is equal to the current instantiation, False otherwise.
        """
        # check if the object other is an instance of the class Task
        if not isinstance(other, Task):
            return False

        # compare identifier, size and execution time
        if not (
            self.identifier == other.identifier
            and self.size == other.size
            and self.execution_time == other.execution_time
        ):
            return False

        # compare A, b, X matrices
        if not (
            np.array_equal(self.A, other.A)
            and np.array_equal(self.b, other.b)
            and np.array_equal(self.X, other.X)
        ):
            return False

        return True


if __name__ == "__main__":
    """
    The main purpose of this example is to demonstrate the execution of a Task. It sets up logging to display DEBUG
    level messages, creates an instance of the Task class with an identifier of 1 and a size of 3000, and then performs
    the task by solving a linear system AX=B using numpy.linalg.solve. The execution time of the task is measured, and
    the solution is printed in DEBUG logging level along with the task identifier. The resulting execution time is
    stored in the 'execution_time' variable.
    """

    # Setting up logging to display DEBUG level messages
    logging.basicConfig(level=logging.DEBUG)

    # Creating a Task instance with identifier 1 and size 3000
    task = Task(1, 3000)

    # Performing the task and measuring execution time
    execution_time = task.work()
