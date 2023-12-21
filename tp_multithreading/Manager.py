from multiprocessing import Queue
from multiprocessing.managers import BaseManager

# global variables for the connection
IP = "localhost"
PORT = 1024
KEY = b"clef tres secrete"

ADDRESS = (IP, PORT)


class QueueManager(BaseManager):
    """
    Custom QueueManager class derived from BaseManager.

    This class can be used to manage shared objects, including queues, across multiple processes.
    Users can register methods for accessing shared resources, such as task and result queues.
    """

    pass


class QueueClient:
    def __init__(self):
        """
        Initializes a queue client with a specified address (composed of an IP and a port) and authentication key.
        """
        # Registering methods for task and result queues in the manager
        QueueManager.register("get_tasks")
        QueueManager.register("get_results")

        # Creating a QueueManager instance with the provided address and authentication key
        manager = QueueManager(address=ADDRESS, authkey=KEY)

        try:
            # Connecting to the manager
            manager.connect()
        except ConnectionRefusedError:
            # Raise ConnectionRefusedError if connection fails
            raise ConnectionRefusedError

        # Assigning task and result queues from the manager to client attributes
        self.tasks = manager.get_tasks()
        self.results = manager.get_results()


if __name__ == "__main__":
    """
    The main purpose of this example is to set up a multiprocessing manager using the QueueManager class. It creates a
    manager instance with a specific address (IP and PORT) and an authentication key. Two methods, "get_tasks" and
    "get_results," are registered with the manager, allowing processes to obtain task and result queues. The server is
    then started to serve forever, waiting for incoming connections and facilitating communication among processes.
    """
    # Creating an instance of QueueManager with specified address and authentication key
    queueManager = QueueManager(address=ADDRESS, authkey=KEY)

    # Registering methods for task and result queues with the QueueManager
    task_queue = Queue()
    result_queue = Queue()
    QueueManager.register("get_tasks", callable=lambda: task_queue)
    QueueManager.register("get_results", callable=lambda: result_queue)

    # Getting the server from the QueueManager and starting it to serve forever
    try:
        queueManager.get_server().serve_forever()
    finally:
        print(
            f"Exiting with {task_queue.qsize()} tasks and {result_queue.qsize()} results remaining"
        )
