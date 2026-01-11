

print("=======================================")

import logging

# Setup
logging.basicConfig(
    filename="calcu.log",
    level=logging.DEBUG,
    format=' %(levelname)s - %(funcName)s(): %(message)s'
)

class Calculator:

    def addition(self, a, b):
        logging.debug(f"addition starts: {a} + {b}")
        result = a + b
        logging.debug(f"Addition complete: {result}")
        return result
    
    def subtract(self, a, b):
        logging.debug(f"Subtraction starts: {a} - {b}")
        result = a - b
        logging.debug(f"Subtracting {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        logging.debug(f"multiplication started: {a} * {b}")
        result = a * b
        logging.debug(f"Multiplication complete: {result}")
        return result

    def divide(self, a, b):
        logging.info(f"divide function started {a} / {b}")
        if b == 0:
            logging.error("cannot divide by Zero")
            return None
        else:
            result = a / b
            logging.debug(f"Division result is {result}")
            return result
    

calc = Calculator()

calc.addition(10, 5)
calc.subtract(20, 8)
calc.multiply(6, 7)
calc.divide(100, 4)
calc.divide(5, 0)



print("=================NB: COMMENTOUT THE FIRST BEFORE TYRING THIS NO2===============")

import logging

# Manual setup logger without the basicConfig model
man_logger = logging.getLogger(__name__)    # # Create a logger

# sets the minimum level of messages the logger will accept.
man_logger.setLevel(logging.DEBUG)

# formatter controls how log messages look
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s: %(funcName)s(): %(message)s')

#A handler decides where the log messages will go.
file_handler = logging.FileHandler('calcu.log') 

# Handler for error logs
# error_handler = logging.FileHandler("error.log")
# error_handler.setLevel(logging.ERROR) # Only Error message will show in file "calcu.log" 

file_handler.setFormatter(formatter)    # Attach the formatter so logs in the file look nic

man_logger.addHandler(file_handler)  # # Add handlers to logger file

#This handler sends logs to the TERMINAL (screen)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

man_logger.addHandler(stream_handler) # Send ALL logs to the terminal

class Calculator:

    def addition(self, a, b):
        man_logger.debug(f"addition starts: {a} + {b}")
        result = a + b
        man_logger.debug(f"Addition complete: {result}")
        return result
    
    def subtract(self, a, b):
        man_logger.debug(f"Subtraction starts: {a} - {b}")
        result = a - b
        man_logger.debug(f"Subtracting {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        man_logger.debug(f"multiplication started: {a} * {b}")
        result = a * b
        man_logger.debug(f"Multiplication complete: {result}")
        return result

    def divide(self, a, b):
        man_logger.info(f"divide function started {a} / {b}")
        if b == 0:
            man_logger.error("cannot divide by Zero")
            return None
        else:
            result = a / b
            man_logger.debug(f"Division result is {result}")
            return result
    

calc = Calculator()

calc.addition(10, 5)
calc.subtract(20, 8)
calc.multiply(6, 7)
calc.divide(100, 4)
calc.divide(5, 0)


print("=======================================")

