<p align="center">

# TP Multithreading

[![License](https://img.shields.io/badge/License-Apache-blue.svg)](https://opensource.org/license/apache-1-1/)
![Test](https://img.shields.io/badge/Test-Succeeded-green)

</p>

## Overview

This Python-based framework facilitates distributed task execution using multiprocessing. The architecture includes a Boss component responsible for task distribution and Minion components that perform assigned tasks. The framework utilizes Python's multiprocessing module and provides a simple way to distribute and process tasks across multiple workers.

## Key Features

- **Boss-Minion Architecture:** Designed for efficient task distribution in a distributed environment.
- **Multiprocessing:** Utilizes Python's multiprocessing capabilities for parallel execution of tasks.
- **Task Management:** Provides classes for managing tasks, results, and communication between the Boss and Minions.
- **Example Implementations:** Includes example implementations for Boss, Minion, and Task classes to help you get started.
- **Unit Tests:** Ensures the reliability and correctness of core functionalities with unit tests.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Launch the  provided `venv_install.sh` script from the _root_ of this project:

   ```bash
   ./setup/venv_install.sh
   ```

### Usage

1. Run the project using the provided `run.py` script  from the _root_ of this project:
   ```bash
   clear & python3 src/run.py
   ```

2. Monitor the output for task execution and results.
3. To exit the program, press `CTRL+C` (several times) to make sure you kill the QueueManager.

## License
This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.
