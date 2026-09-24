# Shared Memory Based Student Result Processing

A Python-based student result processing system that demonstrates Inter-Process Communication (IPC) using shared memory, multiprocessing, and semaphores.

## Overview

This project uses two processes:

- Producer: Stores student marks in shared memory.
- Consumer: Reads the marks from shared memory and calculates the total and average.

Semaphores are used to synchronize the Producer and Consumer processes and ensure that the Consumer reads the data only after it has been stored.

## Concepts Used

- Inter-Process Communication (IPC)
- Shared Memory
- Process Synchronization
- Semaphores
- Multiprocessing
- Producer-Consumer Model

## Technologies

- Python
- `multiprocessing` module

## How It Works

1. The user enters marks for five subjects.
2. A shared array is created to store the marks.
3. The Producer process stores the marks in shared memory.
4. The Consumer waits for the data to become available.
5. The Consumer reads the marks and calculates the total and average.
6. The results are displayed.

## Sample Output

```text
Student Marks: [85, 78, 92, 88, 76]
Total Marks: 419
Average Marks: 83.8
