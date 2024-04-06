import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()

# 괄호를 적절히 쳐서, 이 식의 값을 최소로.

str = input().split('-')
arr = []
for i in str:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    arr.append(sum)

res = arr[0]
for i in range(1,len(arr)):
    res -= arr[i]

print(res)