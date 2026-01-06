
print('======================Context Manager=================')


# Reading
# with open('file.txt', 'r') as f:
#     content = f.read()

# Writing
with open('output.txt', 'w') as f:
    f.write('Hello Python World!')



print('=======================================')
# context manager implements two special methods: __enter__() and __exit__() in its class
# Class 
class File:
    def __init__(self, filename, method):
        self.filename = filename
        self.method = method
        self.file = None

    def __enter__(self):            # This delay the action 
        print('Enter')
        self.file = open(self.filename, self.method)
        return self.file #this will return the enterd file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')
        self.file.close()  # this will run last
        

with File("file1.txt", "w") as f:
    print('Middle')             
    f.write("Hello Python World222!")    # this will run inbetween the enter and exit

print(f.closed)


print('=======================================')
# Creating context managers with contextlib
# The contextlib module provide utilities for creating context managers.
# Using @contextmanager decorator (generator-based)

from contextlib import contextmanager

@contextmanager
def file(filename, method):
    try:
        print('enter')
        file = open(filename, method)
        yield file
    finally:
        file.close()
        print('exit')

with file('file.txt', 'w') as f:
    print('middle')
    f.write('Hello World')


print('================CLASS=======================')

# directory-changing context manager.
import os

cwd = os.getcwd()
os.chdir('files')
print(os.listdir())
os.chdir(cwd)

class ChangeDir:
    def __init__(self, destination):
        self.destination = destination
        self.cwd = None
        

    def __enter__(self):
        self.cwd = os.getcwd()
        os.chdir(self.destination)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.cwd)

with ChangeDir('files'):
    print(os.listdir())
    print(os.getcwd())          # directory we changed to

print(os.getcwd())  # original directory restore


print('============Using GENERATOR=============')
# directory-changing context manager.

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('files'):
    print(os.listdir())
    print(os.getcwd())              # directory we changed to

print(os.getcwd())  # original directory restore

print('=======================================')










