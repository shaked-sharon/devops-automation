# File should hold messages written to log files
# Note to self: Logs will keep track of everything program does

import logging
import os

def setup_logging():
    # Ensures log folder exists and creates it if not
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Sets up logs to be written to file
    logging.basicConfig(
        filename='logs/provisioning.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'  # This means add new messages to the end of the file
    )
    
    # Also want to show messages in the terminal / CLI window
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    
    return logging.getLogger()

# Creates logs that other files can use
logger = setup_logging()
