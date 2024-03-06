import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


n = int(input())
q = deque()

res = []
for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == "push": q.append(int(cmd[1]))
    
    elif cmd[0] == "pop":
        if q: res.append(str(q.popleft()))
        else: res.append("-1")
    
    elif cmd[0] == "size": res.append(str(len(q)))
    
    elif cmd[0] == "empty":
        if q: res.append("0")
        else: res.append("1")
    
    elif cmd[0] == "front":
        if q: res.append(str(q[0]))
        else: res.append("-1")
    
    elif cmd[0] == "back":
        if q: res.append(str(q[-1]))
        else:res.append("-1")

print("\n".join(res))
