# normal checking

a = 7
b = 2

x = 10
y = 10

# Greater than
if a > b:
    print(f"{a} is greater than {b}")
    print("You won")

# in, not, not in, is, is not

# Equality check operator
if x == y:
    print(f"{x} is equal to {y}")

if x is y:
    print(f"{x} is equal to {y}")


if a != b:
    print(f"{a} isn't equal to {b}")

if a is not b:
    print(f"{b} isn't equal to {a}")

isGood = False
if isGood is True:
    print(f"It's {isGood} that you're a good person")
elif isGood is False:
    print(f"It's {not isGood} that you're a bad person")
