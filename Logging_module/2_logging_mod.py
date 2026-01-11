import logging
from logging.handlers import RotatingFileHandler

# Create the main logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # accept INFO and above

# Create a formatter (how each log line will look)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create a rotating file handler
file_handler = RotatingFileHandler(
    'app.log',      # log file name
    maxBytes=1000,  # rotate when file size is about 1000 bytes
    backupCount=3,  # keep up to 3 old log files
    encoding='utf-8'
)
file_handler.setFormatter(formatter)

# Also log to the console (terminal)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
 
# Attach handlers to our logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def process_user(userid: int):
    logger.info(f"Started processing user {userid}")

    if userid % 5 == 0:
        logger.warning(f"User {userid} has missing profile data")

    logger.info(f"Finished processing user {userid}")


# Generate many log lines so rotation can happen
for i in range(1, 50):
    process_user(i)
