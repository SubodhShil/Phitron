# 'max' is a user defined function that used to return
# the maximum value

def maxAge(*args: int):
    maxVal = 1
    for i in args:
        maxVal = max(i, maxVal)
    return maxVal


print(maxAge(33, 2, 70, -1, 9))
print(min(1, -2, -3, 5, 3))


# find length of an array
print(len([1, 2, 3, 5]))
print(sum([1, 2, 3, 5]))

