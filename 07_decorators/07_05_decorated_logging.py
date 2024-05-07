# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

from datetime import datetime

def decorator_func(initial_func):
    def wrapper_func():
        print("the wrapper function picked some...")
        return initial_func()
    return wrapper_func

def time_it(func):
    def time_stamp():
        print(f"The function started at: {datetime.now()}")
        func()
        print(f"The function ended at: {datetime.now()}.")   
    return time_stamp

@time_it
@decorator_func
def prettify():
    print("flowers for you")

prettify()
