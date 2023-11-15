# Accepted
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P

n = int(input())
flag = True
cnt = 0
number_list = list(map(int, input().split()))

while flag:
    for i in range(len(number_list)):
        if number_list[i] % 2 != 0:
            flag = False
            break
        number_list[i] /= 2
    if flag:
        cnt += 1

print(cnt)
