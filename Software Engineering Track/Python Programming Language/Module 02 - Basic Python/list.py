# index    0  1  2  3  4
numbers = [1, 2, 3, 4, 5]
#         -5 -4 -3 -2 -1

print(numbers[-3], numbers[2])

# Simple way to traverse a list
# Syntax: list_identifier[start_index:end_index+1]
# the list will begins from start_index and ends at end_index
# you need to provide +1 to the index you want to stop
print(numbers[0: len(numbers)])

# Traverse way 02
print(numbers[:])

# list[start : end : step]
print(numbers[0: len(numbers): 2])

# traverse in reverse
print("Traverse in reverse Way 1")
print(numbers[len(numbers) - 1: 0:-1])

print("Traverse in reverse Way 2")
print(numbers[::-1])  # shortcut to reverse a list

print("Traverse in reverse Way 3")
i = len(numbers) - 1
while i != -1:
    print(numbers[i])
    i -= 1

# copy number
print("Copied")
numbers2 = numbers[:]
print(numbers2)

# enumerate
print("Index\tValues")
for i, num in enumerate(numbers):
    print(f'{i}\t{num*10}')
