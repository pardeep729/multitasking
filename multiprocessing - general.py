# CPU-intensive programs can share the workload by spawning new interpreters on each CPU core and telling them all to work in parallel
# You can have 1 process and share it amongst all CPU cores, or multiple different processes (e.g. different functions) and they will all share the workload is the most efficient way
# The code structure (in its simplest form) is similar to threading, althought what happens in the backend is verrrrry different
# In the future, learn about pools to see how we can use this module more cleverly

import time

import multiprocessing
from multiprocessing import Process

def homework_1(numbers):
    """
    Sum together all numbers
    """

    result = 0
    for i in numbers:
        print(multiprocessing.current_process().name, "homework_1", i)
        result += i
    return result

def homework_2(numbers):
    """
    Sum of square of all numbers
    """

    result = 0
    for i in numbers:
        print(multiprocessing.current_process().name, "homework_2", i)
        result += i*i 
    return result

def homework_3(numbers):
    """
    Sum of cube of all numbers
    """

    result = 0
    for i in numbers:
        print(multiprocessing.current_process().name, "homework_3", i)
        result += i**3 
    return result




if __name__ == '__main__':
    processlist = []
    numbers = [i for i in range(10**5)]

    processlist.append(Process(target=homework_1, args=(numbers,)))
    processlist.append(Process(target=homework_2, args=(numbers,)))
    processlist.append(Process(target=homework_3, args=(numbers,)))

    # NON-Concurrent version
    start_time = time.time()

    print(homework_1(numbers))
    print(homework_2(numbers))
    print(homework_3(numbers))

    end_time = time.time()
    non_con_duration = end_time - start_time


    # Concurrent version
    start_time = time.time()

    for p in processlist:
        p.start()

    for p in processlist:
        p.join()

    end_time = time.time()
    con_duration = end_time - start_time

    print(f"NON-Concurrent: Took {non_con_duration} seconds.")
    print(f"Concurrent: Took {con_duration} seconds.")