# Lots of CPU intensive work. Lots of processing of data, so just takes time to get through all calculations with 1 CPU core (what threading, asyncio and synchronous programming use).
# Using multiple CPU cores (e.g. multiprocessing) allows you to have more "brains" working on the same task

import time

from concurrent.futures import ThreadPoolExecutor

def cpu_bound(number):
    print(sum(i * i for i in range(number)))

def find_sums(numbers):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound, numbers)

if __name__ == '__main__':
    numbers = [5*(10**6) + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Duration {duration} seconds")