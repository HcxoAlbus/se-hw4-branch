# Design Document

## 1. Overview

This project is a simple Python project designed for Git branch management practice.

The project contains several small modules:

- `main.py`: Program entrance.
- `calc.py`: Arithmetic functions.
- `io_utils.py`: File input and output utilities.
- `model.py`: Task data model.
- `service.py`: Task management service.
- `tests/test_calc.py`: Unit tests for arithmetic functions.

## 2. Module Design

### calc.py

Provides basic arithmetic functions, including addition, subtraction, multiplication, and division.

### io_utils.py

Provides simple file reading, writing, and appending functions.

### model.py

Defines the `Task` class, which represents a task object.

### service.py

Defines the `TaskService` class, which manages a list of tasks.

## 3. Purpose of Branch Management

Different branches can be used to simulate different development directions.

For example:

- B2 may improve calculation functions.
- B3 may improve documentation or configuration.
- C4 may introduce new changes based on B2.

During merging, Git can detect differences and help developers integrate code changes.


## B2 Design Update

In branch B2, the calculation module is extended with additional mathematical functions.
