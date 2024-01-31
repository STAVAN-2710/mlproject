import logging
import os
from datetime import datetime


# Generating a timestamped log file name
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating a path for the logs directory in the current working directory
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# Ensure the logs directory exists
os.makedirs(logs_path,exist_ok=True)

# Setting the full path for the log file within the logs directory
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Configuring the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH, # Path to the log file
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # Log format
    level=logging.INFO,  # Logging level
)

# Now the logging system is set up to log messages to the specified file
# if __name__ == "__main__":
#     logging.info("Logging has started")