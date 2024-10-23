## Multithreading with Thread pool Executor
from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"number: {number}"

numbers = [1,2,3,4,5,6,7,8,9,0,11,12,13]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers,numbers)

for result in results:
    print(result)