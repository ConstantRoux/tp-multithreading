import logging
from typing import Tuple

from Manager import QueueClient
from Task import Task


class Boss(QueueClient):
    def __init__(self, address: Tuple[str, int], authkey: bytes):
        """
        Initializes a Boss instance.

        :param address: The address of the queue manager composed of a string containing the IP and an int containing
        the port.
        :param authkey: The authentication key in bytes.
        """
        super().__init__(address=address, authkey=authkey)

    def put_task(self, identifier: int, size: int):
        """
        Adds a task to the task queue.

        :identifier: The identifier of the task.
        :size: The size of vectors to generate for the linear system.
        """
        # Creating a Task instance with the specified identifier and size
        task = Task(identifier, size)

        # Putting the task into the task queue
        self.tasks.put(task)

        # Logging the addition of the task
        logging.debug(f"Boss added task {identifier} of size {size}")

    def get_result(self, n: int):
        """
        Retrieves and prints results from the result queue.

        :n: The number of results to retrieve.
        """
        for _ in range(n):
            # Getting task identifier and execution time from the result queue
            identifier, execution_time = self.results.get()

            # Printing the result
            print(f"Task {identifier} finished in {execution_time} seconds")


if __name__ == "__main__":
    """
    The main purpose of this example is to demonstrate the usage of the Boss class in interacting with a QueueManager.
    It configures connection parameters (IP, PORT, KEY), sets up logging for debugging, and attempts to connect to the
    QueueManager. If the connection is successful, it logs the success and adds a specified number of tasks (N) to the
    task queue using the `put_task` method of the Boss class. If the connection is refused, it logs an error and exits
    the script with a status of 1.
    """
    # Configuration values for the QueueManager and tasks
    IP = "localhost"
    PORT = 1024
    KEY = b"clef tres secrete"
    N = 10  # Number of tasks
    SIZE = 100  # Size of vectors for tasks

    # Setting up logging to display DEBUG level messages
    logging.basicConfig(level=logging.DEBUG)

    try:
        # Creating a Boss instance and attempting to connect to the QueueManager
        boss = Boss(address=(IP, PORT), authkey=KEY)
        logging.info(f"Connection at ({IP}:{PORT}) with authkey {KEY} succeeded")
    except ConnectionRefusedError:
        # Handling the case where the connection is refused
        logging.error(f"Connection at ({IP}:{PORT}) with authkey {KEY} refused")
        exit(1)

    # Adding tasks to the task queue
    for i in range(N):
        boss.put_task(i, SIZE)
