import logging
from typing import Tuple

from Manager import QueueClient


class Minion(QueueClient):
    def __init__(self, address: Tuple[str, int], authkey: bytes, identifier: int):
        """
        Initializes a Minion instance.

        :param address: The address of the queue manager composed of a string containing the IP and an int containing
        the port.
        :param authkey: The authentication key in bytes.
        :param identifier: The identifier of the minion.
        """
        super().__init__(address, authkey)
        self.identifier = identifier

    def work(self) -> None:
        """
        Performs the work assigned by the Boss.

        Continuously retrieves tasks from the task queue, performs the tasks using the
        'work' method of the Task class, puts the results in the result queue, and logs
        the completion of each task.

        Note: This method runs indefinitely as it continuously processes tasks.
        """
        while True:
            # Get a task from the task queue
            task = self.tasks.get()

            # Perform the task
            task.work()

            # Put the result in the result queue
            self.results.put((task.identifier, task.execution_time))

            # Log the completion of the task
            logging.debug(
                f"Minion {self.identifier} finished task {task.identifier} in {task.execution_time:.2f} seconds"
            )


if __name__ == "__main__":
    """
    The main purpose of this example is to demonstrate the usage of the Minion class in interacting with a QueueManager.
    It configures connection parameters (IP, PORT, KEY), sets up logging for debugging, and attempts to connect to the
    QueueManager using a Minion instance. If the connection is successful, the Minion starts working (processing tasks)
    indefinitely by calling the 'work' method. If the connection is refused, it logs an error and exits the script with
    a status of 1.
    """

    # Configuration values for the QueueManager connection
    IP = "localhost"
    PORT = 1024
    KEY = b"clef tres secrete"

    # Setting up logging to display DEBUG level messages
    logging.basicConfig(level=logging.DEBUG)

    try:
        # Creating a Minion instance and attempting to connect to the QueueManager
        minion = Minion(address=(IP, PORT), authkey=KEY, identifier=1)
    except ConnectionRefusedError:
        # Handling the case where the connection is refused
        logging.error(f"Connection at ({IP}:{PORT}) with authkey {KEY} refused")
        exit(1)

    # Minion starts working (processing tasks) indefinitely
    minion.work()
