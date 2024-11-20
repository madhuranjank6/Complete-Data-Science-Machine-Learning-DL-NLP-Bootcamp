### Multithreading
## When to use Multithreading:
### 1. I/O-bound Tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests)
### 2. Concurrent execution: When we want to improve the thoughput of our application by performing multiple operations concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in "abcdefghi":
        time.sleep(2)
        print(f"Letter: {letter}")

### Creating two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
## Start the threads
t1.start()
t2.start()

### Waiting for the threads to continue
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)