"""
This module provides a decorator to measure the execution time and
memory usage of functions. It helps in analyzing the efficiency of
the conversion process.
"""

from functools import wraps
import time
import tracemalloc


def get_performance(func):
    """
    Decorator function to help measure the time and memory used
    when calling a function
    :param func: the function to be measured
    :return: the wrapper
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        tracemalloc.start()
        results = func(*args, **kwargs)
        end = time.time()

        # only wants to know the max memory used during a call
        _, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return results, (end - start) * 1000, peak_memory / 1024

    return wrapper
