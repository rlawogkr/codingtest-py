import sys
from collections import *

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())

dq = deque()

for i in range(1,n+1):
    dq.append(i)

res = [] #값을 넣을 리스트
#1 2 3 4 5 6 7
#4 5 6 7 1 2 3

dq.rotate(-k)
print(dq)
print(dq.pop())






