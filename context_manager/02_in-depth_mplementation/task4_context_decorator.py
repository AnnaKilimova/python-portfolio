from contextlib import ContextDecorator
import os
import subprocess
from typing import Optional, Type

class SafeExecutor(ContextDecorator):
    '''Security check context decorator'''
    def __enter__(self) -> None:
        '''Executed when entering with before executing the function (when used as a decorator).
        Here, the ALLOW_EXECUTION environment variable is checked.
        '''
        if os.getenv("ALLOW_EXECUTION") == "1":
            print('It works') # Confirmation that execution is permitted.
            subprocess.run(["ls", "-la"]) # Execution of the command.
        else:
            # If the variable is not set or is not equal to ‘1’, execution is prohibited.
            raise ValueError("Выполнение команд запрещено")

    def __exit__(self, exc_type: Optional[Type[BaseException]],exc_val: Optional[BaseException], exc_tb: Optional[object]) -> bool:
        '''Called when exiting the context (after executing the function, if a decorator).
        Here you can handle exceptions and clean up resources.

        :param exc_type: type of exception, if it occurred
        :param exc_val: exception object (error text)
        :param exc_tb: traceback (error information)
        :return:
        '''
        if exc_type:
            print(f"Ошибка {exc_val}") # Display an error message if an error occurs.
        return True # Return True to suppress the exception and not terminate the program abnormally.

# Setting an environment variable that allows code execution.
os.environ["ALLOW_EXECUTION"] = "1"

@SafeExecutor()
def do_sensitive_work():
    '''A function whose execution needs to be monitored.

    :return: None.
    '''
    subprocess.run(["ls", "-la"])

# Function call. Thanks to the decorator, the environment variable will be checked before execution.
do_sensitive_work()

# It is possible to use SafeExecutor as a context manager:
with SafeExecutor():
    do_sensitive_work()




