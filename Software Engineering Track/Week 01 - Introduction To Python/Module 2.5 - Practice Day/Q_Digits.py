# Accepted
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q

t = int(input())

while t:
    num = input()
    revNum = ""
    for i in range(0, len(num)):
        revNum += num[i] + ' '
    print(revNum[::-1])
    t -= 1
