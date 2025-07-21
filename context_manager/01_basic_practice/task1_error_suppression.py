import logging
from typing import Generator, Type
from contextlib import contextmanager

@contextmanager
def suppress_errors(*args: Type[BaseException]) -> Generator[None, None, None]:
    '''Context manager for suppressing specified exceptions.

    :param args: Exceptions that need to be suppressed.
    :return: Context manager that suppresses specified types of errors.
    '''
    try:
        # The code inside the with block is executed here.
        yield
    except args as e:
        # This block will be executed if one of the specified exceptions occurs.
        logging.warning(f"Error of type {type(e).__name__} suppressed: {e}")

with suppress_errors(ZeroDivisionError, ValueError):
    # This code is executed before yield.
    print("That's where all the logic could be.")
    1 / 0
    int("abc")
    print("This will not be executed due to an error.")