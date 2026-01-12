# print('\n=============Multiprocessing=================')
# One program runs multiple processes
# can run truly in parallel on multiple CPU cores
# Good for heavy calculations, big loops, image processing -- CPU-bound tasks (heavy computation)
# Normally Python uses only one core.
# Multiprocessing lets Python use all of them.


# import threading
import multiprocessing
import time



def job():
    print("Job started in 1 day")
    time.sleep(2)
    print("Job finished")

if __name__ == "__main__":
    start = time.time()
    job()
    job()
    job()     
    # calling the job() everytme make them wait for each other and takes long, sychronize
    # Use thread to make them run togther 

    end = time.time()
    print(f"Finished in: {round(end-start, 2)} seconds")   

        




# def job():
#     print("Job started in 1 day")
#     time.sleep(2)
#     print("Job finished")

# if __name__ == "__main__":
#     start = time.time()
#     # create thread
#     p1 = multiprocessing.Process(target=job)
#     p2 = multiprocessing.Process(target=job)

#     # Start threads
#     p1.start()      # tgis runs the process
#     p2.start()

#     # Wait for process to complete
#     p1.join()
#     p2.join()        

#     end = time.time()
#     print(f"Finished in: {round(end-start, 2)} seconds")    




# def job():
#     print("Job started in 1 day")
#     time.sleep(2)
#     print("Job finished")


# if __name__ == "__main__":
#     print('\n===============CPU BOUND===================')

#     start = time.time()
#     # create thread
#     process = []

#     for _ in range(10):
#         p = multiprocessing.Process(target=job)
#         p.start()
#         process.append(p)

#     for pro in process:
#         pro.join()   

#     end = time.time()
#     print(f"Finished in: {round(end-start, 2)} seconds")   




def job(days):
    print(f"Job started in {days} day")
    time.sleep(days)
    print("Job finished")

if __name__ == "__main__":
    print('\n===============FORLOOP FOR MULTIPLE, with argument===================')

    start = time.time()
    # create thread
    process = []

    for _ in range(10):
        
        p = multiprocessing.Process(target=job, args=[3.5]) # arg in process are serialized using pickle args=(10,)
        # p = multiprocessing.Process(target=job, args=(3.5,))  # arg by pickles rgs=(3.5,)
        # That 3.5 is serialized with pickle and sent to the child process
        p.start()
        process.append(p)

    for pro in process:
        pro.join()   

    end = time.time()
    print(f"Finished in: {round(end-start, 2)} seconds")    




import concurrent.futures

def job(days):
    print(f"Job started in {days} day")
    time.sleep(days)
    return f"Job finished {days}"

if __name__ == "__main__":
    print('\n==============Concurrent.futures (as_completed)===================')

    start = time.time()
 
    results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # p = executor.submit(job, 2)     # SUBMIT return a future obj
        # p = executor.submit(job, 2)

        # print(p.result())
        # print(p.result())
        days = [9,5,4,3,2,1]
        for day in days:
            p = executor.submit(job, day)       # Submit return future object
            results.append(p)

        for res in concurrent.futures.as_completed(results):
            print(res.result())

       
    end = time.time()
    print(f"Finished in: {round(end-start, 2)} seconds")    





def job(days):
    print(f"Job started in {days} day")
    time.sleep(days)
    return f"Job finished {days}"

if __name__ == "__main__":
    print('\n==============Concurrent.futures (MAP fuction)===================')

    start = time.time()
 
    with concurrent.futures.ProcessPoolExecutor() as executor:
        days = [16,15,6,5,4,3,2,1]
        results = executor.map(job, days)       # it return the results (in the order they started)

        for res in results:
            print(res)

       
    end = time.time()
    print(f"Finished in: {round(end-start, 2)} seconds")    


    