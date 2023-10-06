# empty class
class Test:
    pass


class Phone:
    price = 25000
    color = 'red'
    brand = 'Samsung'


# Creating an object
my_phone = Phone()
print(my_phone.price)
print(my_phone.color)


# Create class
class Calculator:
    # Create methods
    def addition(self, *args):
        sum: int = 0
        for number in args:
            sum += number
        return sum

    def subtraction(self, a, b):
        return a - b

    def division(self, a, b):
        return a / b

    def multiplication(self, a, b):
        return a * b

# object
calculation1 = Calculator()
print(calculation1.addition(5, 7, 13, 10))
print(calculation1.subtraction(10, 2))
print(calculation1.division(30, 3))
print(calculation1.multiplication(50, 3))
