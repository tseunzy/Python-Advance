


print('==============ITERATORS===============')
# An Iterator is a python object that gives items ONE BY ONE when you ask for them.
# An Iterable is anything you can loop over (using for loop)
# __ITER__ - ITERATOR get their next value with the dunder __NEXT__ method
# we use the iter(object) get iterator and next(iterator) get next item


nums = [11, 5, 3, 14, 51]

iter_nums = iter(nums)      # Get iterator

# print(next(iter_nums))      # Take out first item - 11
# print(next(iter_nums))      # Take out second item - 5
# print(next(iter_nums))
# print(next(iter_nums))
# print(next(iter_nums))
# # print(next(iter_nums))      # Error - StopIteration

# while True:
#     try:
#         iter_nums2 = next(iter_nums)        # Get next item
#         print(iter_nums2)
#     except StopIteration:       # no more items
#         break

for num in iter_nums:       # using forloop
    print(num)

print('==================================')
# # EvenNumbers iterator

class EvenNumbers:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 2       # INCREMENT BY 2 FOR EVEN NUMBERS 
            return value
        else:
            raise StopIteration     # Stop when it get to its limit 
        
evens = EvenNumbers(10)

for num in evens:
    print(num, end=" ")                 # 0 2 4 6 8 10

print('\n==================================')

# iterator of words in a sentence
class Sentence:
    def __init__(self, string):
        self.string = string
        self.word = self.string.split()
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
       
        word = self.word[self.index]
        self.index += 1
        return word
    

my_sentence = Sentence('This is a test')

for sen in my_sentence:
    print(sen)

print('==================================')
# Fibonacci Iterator
class Fibonacci:
    def __init__(self, limit):
        self.count = 0          # current count of generated numbers
        self.a = 0          # first Fibo number
        self.b = 1          # second Fibo number
        self.limit = limit  # wow many numbe to generate

    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.count
        return value
    
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration  # stop when limit reached
        
        if self.count == 0:
            result = self.a      # first number 0
        elif self.count == 1:
            result = self.b      # second number 1
        else:
            result = self.a + self.b
            self.a, self.b = self.b, result  # shift numbers
        
        self.count += 1          # increment counter
        return result

fib = Fibonacci(10)  # Generate first 10 Fibonacci numbers

for num in fib:
    print(num, end=" ")              # 0 1 1 2 3 5 8 13 21 34



print('\n==============GENERATORS===============')
# They hold one result at a time with the yield func, we use the next func to request for the next result
# # EvenNumbers Generator


list_num = [2,4,5,6,7]

def square_num(nums):

    for num in nums:
        yield (num * num)

my_nums = square_num(list_num)

print(next(my_nums))        # hold one result at a time - 4 
print(next(my_nums))        # hold second result 16
print(next(my_nums))        # 25
print(next(my_nums))        # 36

print(next(square_num(list_num)))   # Wrong method - it calls the function afresh: 4
print(next(square_num(list_num)))   # 4

# for num in my_nums:
#     print(num)

print('\n==================================')

list_num = [2,4,5,6,7]
my_num = (x*x for x in list_num)        # () instead of [] makes its a generator
print(my_num)               # Generator- so yu either use NExt or for loop to get the values 
print (list(my_num))        # Convert a Generator to a list [4, 16, 25, 36, 49] - consumes more time 

print('\n==================================')
def even_numbers(limit):
    start = 0
    while start <= limit:
        yield start
        start += 2

for num in even_numbers(10):
    print(num, end=" ")              # 0 2 4 6 8 10


print('\n==================================')
# Generator of words in a sentence

def gen_sentence(sentence):
    index = 0
    word = sentence.split()

    while index < len(word):
        yield word[index]
        index += 1

words = gen_sentence('This is a flower')

for word in words:
    print(word)

print('==================================')
# Fibonacci Generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(f"{next(fib)}")

print('==================================')

# GENERATOR 
def my_range(start, end):
    count = start
    while count < end:
        yield count
        count += 1

nums = my_range(1, 10)

for num in nums:
    print(num, end=' ')                 # 1 2 3 4 5 6 7 8 9


print('\n==================================')
def read_files_good(filenames):
    for filename in filenames:
        with open(filename, 'r') as f:  #  Auto-closes
            yield from f  # yield all lines









