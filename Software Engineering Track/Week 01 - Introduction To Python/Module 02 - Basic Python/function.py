import math


def is_prime(num):
    if num <= 1:
        return False

    limit = int(math.sqrt(num)) + 1
    for i in range(2, limit):
        if num % i == 0:
            return False

    return True


print(is_prime(2))


# positional arguments
# When calling a function, positional arguments should come before keyword arguments

def test(a: int, b: float, *args):
    for arg in args:
        print(arg)


test(10, 3.1416, "Tomar", "nam", "ki")

