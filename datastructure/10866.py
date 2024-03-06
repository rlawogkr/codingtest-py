import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dq = deque()
n = int(input())

res = []
for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push_front":
        dq.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        dq.append(cmd[1])
    elif cmd[0] == "pop_front":
        if dq:
            res.append(str(dq.popleft()))
        else:
            res.append("-1")
            
    elif cmd[0] == "pop_back":
        if dq:
            res.append(str(dq.pop()))
        else:
            res.append("-1")
            
    elif cmd[0] == "size":
        res.append(str(len(dq)))

    elif cmd[0] == "empty":
        if dq:
            res.append("0")
        else:
            res.append("1")
            
    elif cmd[0] == "front":
        if not dq:
            res.append("-1")
        else:
            res.append(str(dq[0]))
    elif cmd[0] == "back":
        if not dq:
            res.append("-1")
        else:
            res.append(str(dq[-1]))

print("\n".join(res))
