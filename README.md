
**ADVANCED PYTHON**

**Iterators & Generators**

    Learn about the dunder __iter__ and the dunder __next__
    The 'ITER' get the iterator and "NEXT" get the first item in the iterable
    In a Generator, the "YIELD" hold one result at a time with the yield function and stop
    Use the "NEXT" to get the result,


**Context managers (with statement)**

    Creating Context managers with Class, __enter__ and __exit__
    Creating Context managers with Generator -- YIELD means “pause here and come back",

**Regular Expressions (Regex)**

    Extract emails, phone numbers, dates, IDs
    Validate inputs (PINs, usernames, passwords)
    Clean text (remove extra spaces, mask numbers)
    Replace patterns safely

**Logging module**

    Simple Logging(DEBUG, INFO, WARNING, ERROR, CRITICAL)
    Multiple Destinations to save logs(for DEBUG, ERROR)
    Rotating File Handler

**Multithreading & Multiprocessing**
    
    Multithreading is a way to run **multiple tasks at the same time** in a single Python program. It is especially useful for tasks that spend a lot of time **waiting**, like:
    - downloading files from the internet, reading/writing files
    - calling APIs, database queries
    Threading Tool - threading` module
    concurrent.futures.ThreadPoolExecutor
    Example: Multithreaded PDF Downloader

    Multiprocessing is a way to run tasks **in parallel using multiple CPU cores**.  
    Unlike multithreading (which shares one process), multiprocessing creates **separate processes**, each with its own Python interpreter and memory space.
    Multiprocessing Tools - multiprocessing module
    concurrent.futures.ProcessPoolExecutor


[Corey Schafer](https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
