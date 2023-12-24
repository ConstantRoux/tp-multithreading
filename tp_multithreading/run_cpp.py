import logging
import subprocess
import time
from multiprocessing import Process, Queue

import proxy
from Boss import Boss
from Manager import ADDRESS, IP, KEY, PORT, QueueManager


def start_manager():
    # Creating an instance of QueueManager with specified address and authentication key
    queueManager = QueueManager(address=ADDRESS, authkey=KEY)
    logging.debug("Queue manager launched")

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


def start_proxy():
    logging.debug("Proxy launched")
    proxy.run()


def start_minion(identifier: int):
    subprocess.Popen(["build/low_level"])
    logging.debug(f"Minion {identifier} launched")


if __name__ == "__main__":
    #############
    # Variables #
    #############
    # Boss configuration values
    N = 20  # Number of tasks
    SIZE = 2000  # Size of vectors for tasks

    # Minion configuration values
    M = 10  # Number of minions

    ###########
    # Logging #
    ###########
    # Setting up logging to display DEBUG level messages
    logging.basicConfig(level=logging.DEBUG)
    print(
        "Logging activated, press CTRL+C (several times) at any time to stop the script and kill the manager"
    )

    ###########
    # Manager #
    ###########
    # Start the manager and keep his PID to kill it later
    p_manager = Process(
        target=start_manager,
    )
    p_manager.start()

    # Wait the manager to get started
    time.sleep(1)

    #########
    # Proxy #
    #########
    # Start the manager and keep his PID to kill it later
    p_proxy = Process(
        target=start_proxy,
    )
    p_proxy.start()

    # Wait the proxy to get started
    time.sleep(1)

    ########
    # Boss #
    ########
    # Set the task in the queue
    try:
        # Creating a Boss instance and attempting to connect to the QueueManager
        boss = Boss()
        logging.info(
            f"Connection of boss at ({IP}:{PORT}) with authkey {KEY} succeeded"
        )
    except ConnectionRefusedError:
        # Handling the case where the connection is refused
        logging.error(f"Connection of boss at ({IP}:{PORT}) with authkey {KEY} refused")
        exit(1)

    # Adding tasks to the task queue
    for i in range(N):
        boss.put_task(i, SIZE)

    ###########
    # Minions #
    ###########
    for i in range(M):
        p_m = Process(target=start_minion, args=(i,))
        p_m.start()

    #############
    # Main loop #
    #############
    while True:
        try:
            pass
        except KeyboardInterrupt:
            # Kill the manager will kill all the minions
            p_manager.kill()
            print("Manager killed")

            # Kill the proxy will kill all the minions
            p_proxy.kill()
            print("Proxy killed")
