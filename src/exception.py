import sys
import logging
import logger

# whenever an error occurs i want my own custom message
# has two parameters - error, and the error detail that is present with the sys.

def error_message_detail(error, error_detial:sys):
    _, _, exc_tb = error_detial.exc_info()   # Unpacks the tuple, only keeping the traceback part
    # the exc_info gives 3 sections of information out of which only the third one is important.
    # exc_tb tells us in which file the exception has occured and in wich line
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error) )
    
    return error_message
    

# Custom Exception class inheriting from Python's Exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detial:sys):
        super().__init__(error_message)  # Initializing the base Exception class
        # Creating a detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detial = error_detial) # Create error message


    def __str__(self):                       # Define how the object is represented as a string
        return self.error_message            # Return the error message
    


        
