print("=======================================")
# It's part of the standard library and provides a better alternative to print() statements for production code.
# Logging records everything so you can investigate later.

# DEBUG	        Detailed info, detailed information
# INFO	        General program flow when working correctly
# WARNING	    Something might be wrong
# ERROR	        Something failed
# CRITICAL	    Program is in danger, a serious error 


# Default level is set to Warning - means that
#  it will capture every level below which are ERROR and CRITICAL and ignore DEBUG and INFO

print("=======================================")
import logging

logging.basicConfig(level=logging.DEBUG)      # Setup logging

# BY default, level=logging.WARNING             # Setup logging

logging.debug("Program started")        # Doesnt pass the message
logging.info("Program started")
logging.warning("Low disk space")
logging.error("Something went wrong")
logging.critical("Program started")
print("=======================================")



logging.basicConfig(level=logging.INFO)         # Setup logging (the level set above will overight this level)

def add(a, b):
    logging.info("add() function started {a} + {b}")
    result = a + b
    logging.info(f"Result is {result}")
    return result

add(5, 3)

print("=======================================")

logging.basicConfig(level=logging.INFO)  # Setup logging

def divide(a, b):
    logging.info("divide() function started {a} / {b}")
    if b == 0:
        logging.error("cannot divide by Zero")
        return None
    else:
        result = a / b
        logging.info(f"Division result is {result}")
        return result
    
divide(10, 2)


print("=======================================")
logging.basicConfig(level=logging.ERROR)

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("An error occurred")



print("===============Logging to a File========================")
# NB: COMMENT OUT THE FIRST BEFORE TYRING THIS NO2
# Logging to a File from a Function

import logging

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def login(user):
    logging.info(f"User {user} logged in")

login("TImothy")


print("===============Logging to a File 2========================")
import logging

# Simple setup
# logging.basicConfig(filename="test.log", level=logging.INFO, format='%(levelname)s: %(message)s')

def add_num(a, b):
    logging.info(f"addition starts: {a} + {b}")
    result = a + b
    logging.info(f"Addition complete: {result}")
    return result

def multiply(a, b):
    logging.info(f"multiplication started: {a} * {b}")
    result = a * b
    logging.info(f"Multiplication complete: {result}")
    return result

def divide(a, b):
    logging.info(f"divide() function started {a} / {b}")
    if b == 0:
        logging.error("cannot divide by Zero")
        return None
    else:
        result = a / b
        logging.info(f"Division result is {result}")
        return result
    

sum_result = add_num(5, 3)
product_result = multiply(4, 6)
div_result = divide(24, 6)

print(f"Sum: {sum_result}")
print(f"Product: {product_result}")
print(f"Divide: {div_result}")














# Default level is set to Warning - means that
#  it will capture every level below which are ERROR and CRITICAL and ignore DEBUG and INFO


# DEBUG	        Detailed info, detailed information
# INFO	        General program flow when working correctly
# WARNING	    Something might be wrong
# ERROR	        Something failed
# CRITICAL	    Program is in danger, a serious error 

# %(asctime)s   time
# %(levelname)s INFO, ERROR
# %(message)s   your message
# %(filename)s  file name
# %(lineno)d    line numbe

# Logging is like a CCTV camera for your program.
# It records everything so you can investigate later.
# With logging:
# You can save to a file
# You can filter messages
# You can turn logs off easily
# You can add timestamps