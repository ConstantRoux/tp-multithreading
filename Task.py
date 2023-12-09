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
        self.execution_time = None

    def work(self) -> float:
        """
        Performs the task by solving a linear system AX=B.

        Generates random vectors a and b of the specified size, solves the linear system AX=B using numpy.linalg.solve,
        measures the execution time, and prints in DEBUG the solution.

        :return: The execution time of the task in seconds.
        """
        # generate random vectors a, b of size size
        a = np.random.rand(self.size, self.size)
        b = np.random.rand(self.size)

        # solve linear system ax=b and measure start and stop time
        start_time = perf_counter()
        np.linalg.solve(a, b)
        end_time = perf_counter()

        # compute execution time
        self.execution_time = end_time - start_time

        # print the task id and the execution time in DEBUG logging level
        logging.debug(f"Task {self.identifier}: {self.execution_time:.2f} seconds")

        # return execution time
        return self.execution_time


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
