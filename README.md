<p align="center">

# TP Multithreading

[![License](https://img.shields.io/badge/License-Apache-blue.svg)](https://opensource.org/license/apache-2-0/)
![Test](https://img.shields.io/badge/Test-Succeeded-green)

</p>

## Overview

This framework supports distributed task execution using either Python or C++ via a proxy and JSON for faster processing. The architecture includes a Boss component responsible for task distribution and Minion components that carry out assigned tasks. The framework leverages Python's multiprocessing module and provides a straightforward way to distribute and process tasks across multiple workers.

## Key Features

- **Boss-Minion Architecture:** Designed for efficient task distribution in a distributed environment.
- **Multiprocessing:** Utilizes Python's multiprocessing capabilities for parallel execution of tasks.
- **Task Management:** Provides classes for managing tasks, results, and communication between the Boss and Minions.
- **Example Implementations:** Includes example implementations for Boss, Minion, and Task classes to help you get started.
- **C++ Integration:** Supports integration with C++ Minions via a proxy and JSON for faster processing.
- **Unit Tests:** Ensures the reliability and correctness of core functionalities with unit tests.

## Getting Started

### Prerequisites

- Linux OS
- Python 3.x

### Installation
1. Launch the  provided `venv_install.sh` script from the _root_ of this project:

   ```bash
   ./setup/venv_install.sh
   ```
2. Build and compile the C++ part from the _root_:
   ```commandline
   cmake -B build -S .
   cmake --build build/
   ```

### Usage

1. Run the project using the provided `run_py.py` (for Numpy) or `run_cpp.py` (for Eigen) scripts from the _root_ of this project:
   ```bash
   clear & python3 tp_multithreading/run_py.py
   ```
   or
   ```bash
   clear & python3 tp_multithreading/run_cpp.py
   ```

2. Monitor the output for task execution and results.
3. To exit the program, press `CTRL+C` (several times) to make sure you kill the QueueManager.

### Examples

1. Example of `run_py.py` with 5 tasks, 2 minions and size's problem of 2000:
   ```cmd
   $ python tp_multithreading/run_py.py
   Logging activated, press CTRL+C (several times) at any time to stop the script and kill the manager
   DEBUG:root:Queue manager launched
   INFO:root:Connection of boss at (localhost:1024) with authkey b'clef tres secrete' succeeded
   DEBUG:root:Boss added task 0 of size 2000
   DEBUG:root:Boss added task 1 of size 2000
   DEBUG:root:Boss added task 2 of size 2000
   DEBUG:root:Boss added task 3 of size 2000
   DEBUG:root:Boss added task 4 of size 2000
   DEBUG:root:Connection of minion 0 at (localhost:1024) with authkey b'clef tres secrete' succeeded
   DEBUG:root:Connection of minion 1 at (localhost:1024) with authkey b'clef tres secrete' succeeded
   DEBUG:root:Task 0: 1.79 seconds
   DEBUG:root:Minion 0 finished task 0 in 1.79 seconds
   DEBUG:root:Task 1: 1.77 seconds
   DEBUG:root:Minion 1 finished task 1 in 1.77 seconds
   DEBUG:root:Task 2: 1.79 seconds
   DEBUG:root:Minion 0 finished task 2 in 1.79 seconds
   DEBUG:root:Task 3: 1.77 seconds
   DEBUG:root:Minion 1 finished task 3 in 1.77 seconds
   DEBUG:root:Task 4: 1.76 seconds
   DEBUG:root:Minion 0 finished task 4 in 1.76 seconds
   ^CExiting with 0 tasks and 5 results remaining
   ```

2. Example of `run_cpp.py` with 5 tasks, 2 minions and size's problem of 2000:
   ```cmd
   $ python tp_multithreading/run_cpp.py

   Logging activated, press CTRL+C (several times) at any time to stop the script and kill the manager
   DEBUG:root:Queue manager launched
   DEBUG:root:Proxy launched
   INFO:root:Connection of boss at (localhost:1024) with authkey b'clef tres secrete' succeeded
   DEBUG:root:Boss added task 0 of size 2000
   DEBUG:root:Boss added task 1 of size 2000
   DEBUG:root:Boss added task 2 of size 2000
   DEBUG:root:Boss added task 3 of size 2000
   DEBUG:root:Boss added task 4 of size 2000
   DEBUG:root:Minion 1 launched
   DEBUG:root:Minion 0 launched
   127.0.0.1 - - [24/Dec/2023 14:49:04] "GET / HTTP/1.1" 200 -
   127.0.0.1 - - [24/Dec/2023 14:49:07] "GET / HTTP/1.1" 200 -
   Minion 34187 for task 0 initialized
   Minion 34187 finished task 0 in 0.331167 seconds
   127.0.0.1 - - [24/Dec/2023 14:49:11] "GET / HTTP/1.1" 200 -
   Minion 34186 for task 1 initialized
   Minion 34186 finished task 1 in 0.331505 seconds
   127.0.0.1 - - [24/Dec/2023 14:49:14] "GET / HTTP/1.1" 200 -
   Minion 34187 for task 2 initialized
   Minion 34187 finished task 2 in 0.34753 seconds
   127.0.0.1 - - [24/Dec/2023 14:49:18] "GET / HTTP/1.1" 200 -
   Minion 34186 for task 3 initialized
   Minion 34186 finished task 3 in 0.334038 seconds
   127.0.0.1 - - [24/Dec/2023 14:49:21] "GET / HTTP/1.1" 200 -
   Minion 34187 for task 4 initialized
   Minion 34187 finished task 4 in 0.323461 seconds
   ^CManager killed
   Proxy killed
   ```

**Note:** we can see that the tasks performed by C++ code are much faster than those performed by Python, which is expected.


## License
This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.
