### Mutliprocessing
### It allows us to create the process that run in parallel

### When to use?:
### 1. CPU-Bound Tasks: Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing, etc)
### 2. Parallel execution: If we want to use multiple cores of the CPU


import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i}: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube of {i}: {i**3}")

## Creating two process
p1 =  multiprocessing.Process(target=square_numbers)
p2 = multiprocessing.Process(target=cube_numbers)

if __name__ == "__main__":
    t = time.time()
    ## Start the process
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)

