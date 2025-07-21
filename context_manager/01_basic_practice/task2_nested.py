from contextlib import contextmanager
from typing import Generator

# Global variable for storing the current file.
log_file = None

@contextmanager
def open_log_file(filename:str) -> Generator[None, None, None]:
    '''Context manager for working with a file in write mode.

    :param filename: The name of the file being transferred.
    :return: Context manager for file recording.
    '''
    # Creating a variable that is visible outside the function.
    global log_file

    # Opening a log file in write mode.
    file_log = open(filename, "w")
    # Passing a file to a global variable for use in other context managers
    log_file = file_log
    try:
        # Writing data to a file.
        log_file.write("Log opened\n")
        # Return of context control.
        yield log_file
    finally:
        # Guaranteed file closure.
        log_file.close()

@contextmanager
def open_data_file(filename:str) -> Generator[None, None, None]:
    '''Context manager for working with data files in read and write mode.

        :param filename: The name of the file being transferred.
        :return: Context manager for file recording.
        '''
    # Opening a file with data in read and write mode.
    data_file = open(filename, "w+")
    try:
        # Writing data to a file that was opened using another context manager.
        if log_file:
            log_file.write("Data file opened\n")
        yield data_file
    finally:
        # Return of context control.
        data_file.close()

# Working with context managers.
with open_log_file("log.txt") as log:
    with open_data_file("data.txt") as data:
        data.write("Data recording\n")