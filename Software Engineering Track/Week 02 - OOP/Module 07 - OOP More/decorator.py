import math
import time

# Wrapper function
# Example 1
def timer(function_arg):
    def inner(*args, **kwargs):
        start = time.time()
        print(f"Time started at {start}")
        function_arg(*args, **kwargs)
        end = start + time.time()
        print(f"Time ended at {end}")
        print(f"Total execution time {end - start}")

    return inner

# timer()()

@timer
def getFactorial(n):
    print("Factorial")
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")

getFactorial(6)

# Example 2
def outer_func(func_as_arg):
    def inner_func_wrapper():
        # additional task
        print("additional task 1")

        # invoking parameter function
        func_as_arg()

        # additional task
        print("additional task 2")

    return inner_func_wrapper

@outer_func
def test():
    print("Testing")

# outer_func(test)()
# test()