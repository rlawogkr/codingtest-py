import sys
from collections import *

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())

dq = deque()

for i in range(1,n+1):
    dq.append(i)

res = [] #값을 넣을 리스트
while len(dq) != 0:
    dq.rotate(-k)
    res.append(dq.pop())

print("<"+", ".join(map(str, res))+ ">")