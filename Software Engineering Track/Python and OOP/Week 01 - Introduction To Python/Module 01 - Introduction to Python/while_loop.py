# Type 1
count = 1
while count is not 11:
    print(count)
    count += 1

# Type 2
count = 1
while count < 11:
    print(count)
    count += 1

numbers = [1, 2, 11, 33, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# For loop
sum = 0
print("Using for loop")
for num in numbers:
    sum += num

print(f"sum is {sum}")

# For loop using range
# range(inclusive_i, exclusive_i, interval_steps)
i = 0
for i in range(0, 5, 2):
    print(numbers[i])
