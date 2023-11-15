# multi return by default return in a tuple

def multiReturn(name, age:int, isMarried:bool):
    return name, age, isMarried

print(multiReturn("Subodh", 23, False))

# multiple value can be returned in a list
def multiReturnList(a:int, b:float, c:str):
    return [b, c, a]
print(multiReturnList(11, 33.2, "tomar nam ki"))


# multiple value can also be returned in a dictionary
def multiReturnList(a:int, b:float, c:str):
    return {a, c, b}

print(multiReturnList(11, 33.2, "tomar nam ki"))
