
print('\n=============EXAMPLE 1====================')
import time
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

end = time.time()
print(f"Finished in {round((end - t), 2)} seconds")
print("Both threads finished!")

print('\n==========Using ThreadPoolExecutor=======================')

import concurrent.futures
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1: {i}")
    return "Numbers thread finished"

def print_characters():
    for char in 'ABCDE':
        time.sleep(1)
        print(f"Thread 2: {char}")
    return "Characters thread finished"

start = time.time()

# Create ThreadPoolExecutor with 2 workers (one for each task)
# max_workers is a thread that does a job - Create a pool of 10 threads that can work at the same time.
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:  
    # Submit both functions for execution
    f1 = executor.submit(print_numbers)
    f2 = executor.submit(print_characters)
    
    # Wait for both to complete and get results
    print(f1.result())
    print(f2.result())

end = time.time()
print(f"Finished in {round((end - start), 2)} seconds")


print('\n==========Example 2=======================')

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()
#calc_square(arr) 
#calc_cube(arr)

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(f"Finished in : {round((end-t),2)} seconds")

print('\n==========Using ThreadPoolExecutor=======================')

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:',n*n)
    return "Square of numbers"

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:',n*n*n)
    return "Cube of numbers"

arr = [2,3,8,9]

start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    f1 = executor.submit(calc_square, arr)
    f2 = executor.submit(calc_cube, arr)

    print(f1.result())
    print(f2.result())

end = time.time()
print(f"Finished in {round((end - start), 2)} seconds")
