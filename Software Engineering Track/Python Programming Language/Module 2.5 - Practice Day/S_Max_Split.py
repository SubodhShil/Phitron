str = input()
cnt: int = 0
tempStr = ""
currentChar = str[0]
stringList = []

for char in str:
    if currentChar == char:
        tempStr += char
        cnt += 1
    else:
        tempStr += char
        cnt -= 1

    if cnt == 0:
        stringList.append(tempStr)
        tempStr = ""
        currentChar = char

print(len(stringList))
for item in stringList:
    print(item)
