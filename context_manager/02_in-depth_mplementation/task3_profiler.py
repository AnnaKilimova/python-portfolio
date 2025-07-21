import time
from typing import  Any

class Profiler:
    '''Context manager Profiler'''
    level = 0  # Global nesting level for all instances.

    def __init__(self:object, block_name:str) -> None:
        '''Initialisation of profiler with block name.

        :param block_name: The name of the block that will be recorded in the log.
        '''
        self.block_name = block_name

    def __enter__(self:object) -> "Profiler":
        '''Starts when entering the with block.

        :return: The current instance of Profiler.
        '''
        Profiler.level += 1
        # Indentation level for tracking profile nesting.
        self.indent = " " * (Profiler.level - 1)
        # Start of block execution time.
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type:Any, exc_val:Any, exc_tb:Any) -> None:
        '''The method is launched when exiting the with block, even if an exception occurs.

        :param exc_type: Exception type || None.
        :param exc_val: Exception value || None.
        :param exc_tb: Stack trace object || None.
        :return: None - does not suppress exceptions.
        '''
        # Start of block execution time.
        end_time = time.perf_counter()
        # Total execution time of the block.
        duration = end_time - self.start_time
        # Recording the execution time of a block in a file, taking into account nesting.
        with open("profile.log", "a") as f:
            f.write(f"{self.indent}Блок '{self.block_name}' — {duration:.3f} сек\n")
        # Decrement for tracking nesting.
        Profiler.level -= 1

def some_heavy_function():
    time.sleep(0.1)

# Working with context managers.
with Profiler("outer"):
    some_heavy_function()
    with Profiler("inner"):
        time.sleep(0.2)
        with Profiler("inner_inner"):
            time.sleep(0.1)

