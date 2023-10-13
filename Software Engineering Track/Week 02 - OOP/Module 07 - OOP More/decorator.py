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