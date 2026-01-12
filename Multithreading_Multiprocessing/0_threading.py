

print('\n=============Multithreading=================')

# one program runs multiple threads (small workers) inside the same process
# Threads share the same memory
#  Good for downloading files, waiting for network, reading file -- I/O-bound tasks (waiting tasks)


import threading
import time


def job():
    print("Job started")
    time.sleep(2)
    print("Job finished")


start = time.time()
job()
job()
job()     
# calling the job() everytme make them wait for each other and takes long, sychronize
# Use thread to make them run togther 

end = time.time()
print("Main program continues")
print(f"Finished in: {round(end-start, 2)} seconds")        # Finished in: 6.0 seconds


print('\n=======threading using Threading (start/JOin)==============')


def job():
    print("Job started")
    time.sleep(2)
    print("Job finished")


start = time.time()


# create thread
t1 = threading.Thread(target=job)
t2 = threading.Thread(target=job)

# Start threads
t1.start()      # tgis runs the thread
t2.start()

# Wait for threads to complete
t1.join()
t2.join()        # this finished together in 2.00253 seconds

end = time.time()
print("Main program continues")
print(f"Finished in: {round(end-start, 2)} seconds")    # Finished in: 2.0 seconds


print('\n===========Creating multiple thread using loop)==============')


def job():
    print("Job started")
    time.sleep(2)
    print("Job finished")


start = time.time()

# Instead of manually creating each thread, we can create thread in a loop
# Create a for loop to start each of the threads
threads = []
for _ in range(10): # (_) is a throwaway variable 
    t = threading.Thread(target=job)
    t.start()
    threads.append(t)

# To run join on all of the started thread in the list of threads
for thread in threads:
    thread.join()

end = time.time()
print("Main program continues")
print(f"Finished in: {round(end-start, 2)} seconds")       # Finished in: 2.01 seconds


print('\n=============with argument)=================')

def job(days):
    print(f"Job started in {days} days")
    time.sleep(days)
    print(f"Job finished in {days} days")


start = time.time()

# Instead of manually creating each thread, we can create thread in a loop
# Create a for loop to start each of the threads
threads = []
for _ in range(10): # (_) is a throwaway variable 
    t = threading.Thread(target=job, args=[3.5])       # arg is passed as a list
    t.start()
    threads.append(t)

# To run join on all of the started thread in the list of threads
for thread in threads:
    thread.join()

end = time.time()
print("Main program continues")
print(f"Finished in: {round(end-start, 2)} seconds")       # Finished in: 2.01 seconds



print('\n=============Concurrent.futures)=================')
import concurrent.futures
import time

def job(days):
    print(f"Job started in {days} days")
    time.sleep(days)
    return(f"Job finished in {days} days")

start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(job, 2)        # SUbmit schedule a funct to exe and return a future obj
    f2 = executor.submit(job, 2)
    print(f1.result())
    print(f2.result())

end = time.time()
print(f"Finished in: {round(end-start, 2)} days")


print('\n==========Using for loop for each SUBMIT with .as_completed============')
import concurrent.futures
import time

def job(days):
    print(f"Job started in {days} days")
    time.sleep(days)
    return(f"Job finished in {days} days")

start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
  
    # Instead of manually creating each thread, we can create thread in a loop
    # Create a for loop to start each of the threads
    dayss = [5, 4, 3, 2, 1]
    results = []

# ✅ Futures - When you submit a task, it returns a **Future** object:
    for day in dayss:           # SUBMIT method return the future object
        future = executor.submit(job, day)
        results.append(future)

# ✅ `as_completed()` - This allows you to process results as soon as each thread finishes:\
    for f in concurrent.futures.as_completed(results):
        print(f.result())


    # dayss = [5,4,3,2,1]       # using list comprehension direct
    # results = [executor.submit(job, day) for day in dayss]
    # for f in concurrent.futures.as_completed(results):
    #    print(f.result())


end = time.time()
print(f"Finished in: {round(end-start, 2)} days")

print('\n============concurrent.futures, using "map" function)=================')
import concurrent.futures
import time

def job(days):
    print(f"Job started in {days} days")
    time.sleep(days)
    return(f"Job finished in {days} days")

start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    dayss = [5, 4, 3, 2, 1]
    results = executor.map(job, dayss)  # the map return the result in the order they started

    for res in results:
        print(res)

end = time.time()
print(f"Finished in: {round(end-start, 2)} days")



print('\n=============Example=================')

import threading 

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1: {i}")

def print_characters():
    for char in 'ABCDE':
        time.sleep(1)
        print(f"Thread 2: {char}")

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_characters)

# Start threads
t = time.time()
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

print("Finished in", time.time()-t)
print("Both threads finished!")












