# Example = making breakfast
# You can start off some or all of the steps (e.g. toast bread, boil eggs. etc.)
# Then you work on some while waiting for others (e.g. fry eggs while kettle is boiling)
#   Doesn't have to be "time.wait", but any method/function/process that has idle time (e.g. API calls)
# So a single brain (CPU core) but multiple trains of thought (threads)
# In the future, learn about pools to see how we can use this module more cleverly


import time

from threading import Thread

# Functions to be called
def toast_bread():
    print("toasting bread..")
    time.sleep(8)
    print("bread toasted")

def make_some_coffee():
    print("turned on coffee maker..")
    time.sleep(4)
    print("Poured a nice cup of coffee")

def boil_water_and_egg():
    print("boiling water..")
    time.sleep(5.5)
    print("water boiled")


# Store our thread definitons
threadlist = []

# Populate with threads
threadlist.append(Thread(target=toast_bread))
threadlist.append(Thread(target=make_some_coffee))
threadlist.append(Thread(target=boil_water_and_egg))

if __name__ == '__main__':
    # NON-Concurrent version
    start_time = time.time()

    toast_bread()
    make_some_coffee()
    boil_water_and_egg()

    end_time = time.time()
    print(f"NON-concurrent: Took {end_time-start_time} seconds.")

    
    # Concurrent (threading) version
    start_time = time.time()

    # Start all threads, a thread will run when others are waiting
    for t in threadlist:
        t.start()

    # Wait for them all to finish
    for t in threadlist:
        t.join()

    end_time = time.time()
    print(f"Concurrent: Took {end_time-start_time} seconds.")



