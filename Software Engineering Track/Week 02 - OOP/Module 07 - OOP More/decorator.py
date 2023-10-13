# Wrapper function
# Example 1
def timer(function_arg):
    def inner():
        print("Time started")
        print(function_arg)
        print("Time ended")
    return inner

# timer()()

@timer
def getFactorial():
    print("Factorial")

# getFactorial()

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

test()
