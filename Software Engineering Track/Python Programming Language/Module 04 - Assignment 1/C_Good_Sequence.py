n = int(input())

number_list = list(map(int, input().split()))
element_frequency = {}
removeCnt = 0

for item in number_list:
    if item in element_frequency:
        element_frequency[item] += 1
    else:
        element_frequency[item] = 1

for key, value in element_frequency.items():
    if value > key:
        removeCnt += (value - key)
    if key > value:
        removeCnt += value

print(removeCnt)
