def sum(num1, num2, *numbers):
    sum = num1 + num2
    for num in numbers:
        sum += num
    return sum


# print(sum(1, 2, 33))
# print(sum(num1=11, num2=50))

""" args """
def chapriNames(name1, name2, *names):
    for name in names:
        print(name)

    print(name1, name2)


# chapriNames("Alice", "Bob", "Nimbda", "Toktok")

""" kwargs """
def studentsName(name1, name2, **otherNames):
    print(name1, name2)

    for key, name in otherNames.items():
        print(key, name)


# studentsName(name1="Pakhi", name2="Rakhi", a="Subodh", b="Antu", c="Rambi")
