'''
Real-World Example: Multiprocessing for CPU-bound tasks
Scenario: Factorial calculation
Factorial Calculations, especially for the large numbers, involving significant computational work. Multiprocessing can be used to distribute the workload across multiple cpu cores, improving performance.
'''

import multiprocessing
import math
import sys
import time

## Increase the maximum number of digits for the integer conversion
sys.set_int_max_str_digits(1000000)

## Function to compute the factorial of a given number
def compute_factorial(number):
    print(f"Factorial of {number}")
    result = math.factorial(number)
    print(f"factorial of {number} id {result}")
    return result

if __name__ == "__main__":
    numbers = [5000,6000,700,8000]
    start_time = time.time()
    ## Creating the pool of workers
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,numbers)

    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken: {end_time-start_time}")