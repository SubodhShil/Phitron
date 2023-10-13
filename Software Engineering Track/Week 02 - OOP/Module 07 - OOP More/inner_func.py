def main_func():
    print("Main function body")

    def inner_func():
        print("Inner function body")
        return "This is inner function"
    result = inner_func()

    return result

def hola(pass_func):
    return pass_func

def message(msg):
    return msg

print(message('message says hola'))
print(main_func())

