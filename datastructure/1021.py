import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())  # n: 큐의 크기, m:뽑아내려고 하는 수의 개수
dq = deque()

for i in range(1, n + 1):
    dq.append(i)

values = [int(i) for i in input().split()]

count = 0

for val in values:
    while True:
        if dq[0] == val:
            dq.popleft()
            break
        else:
            if dq.index(val) > len(dq) // 2:
                dq.rotate(+1)
                count += 1
            else:
                dq.rotate(-1)
                count += 1

print(count)
