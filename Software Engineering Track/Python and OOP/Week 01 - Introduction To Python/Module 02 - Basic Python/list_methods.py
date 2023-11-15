# append -> adding or push new element at end of the list
numbers = [11, 12, 13, 14, 15]
print(numbers[:])
numbers.append(16)
print(numbers[:])

# insert -> adding element at a specific position
numbers.insert(2, -8)
print(numbers[:])

numbers.append(22)
numbers.append(-22)
numbers.append(22)
print(numbers[:])

# remove -> deletes the first occurrence from the list
# you should always check the element to be deleted available in the list, otherwise it will throw error
if 22 in numbers:
    numbers.remove(22)
print(numbers[:])

# pop -> remove the last element
numbers.pop()
print(numbers[:])

# sort values
numbers.sort()
print(numbers[:])

# descending order sorting in one go
numbers.sort(reverse=True)
print(numbers[:])
