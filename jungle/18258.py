import sys
from collections import deque

input = sys.stdin.readline
dq = deque()
n = int(input().rstrip())

for _ in range(n):
    command = input().rstrip().split()
    if len(command) == 2:
        command[1] = int(command[1])
    
    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'pop':
        if not dq: print(-1)
        else: print(dq.popleft())
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if not dq: print(1)
        else: print(0)
    elif command[0] == 'front':
        if not dq: print(-1)
        else: print(dq[0])
    elif command[0] == 'back':
        if not dq: print(-1)
        else: print(dq[-1])
