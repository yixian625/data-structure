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

        # avoid doing try except again in driver
        try:
            result = func(*args, **kwargs)
            status = "Success"

        except Exception as e:
            # want to return any error message if function fails
            result = f"Error: {str(e)}"
            status = "Error"

        # capture time & memory regardless of function error
        finally:
            end = time.time()
            # only wants to know the max memory used during a call
            _, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

        # returning results and time in ms, memory used in KB
        return result, status, (end - start) * 1000, peak_memory / 1024

    return wrapper
