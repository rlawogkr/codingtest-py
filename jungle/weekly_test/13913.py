import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def move(location,i):
    if i == 0:
        return location-1
    elif i == 1:
        return location+1
    else:
        return 2*location

_list = [0 for _ in range(100001)]
_visited = [False for _ in range(100001)]
def bfs(x):
    dq = deque()
    dq.append(x)
    _visited[x] = True

    while dq:
        val = dq.popleft()

        for i in range(3):
            nx = move(val, i)
            if nx >=0 and nx <= 100000 and _visited[nx] == False:
                _visited[nx] = True
                _list[nx] = _list[val] + 1
                dq.append(nx)



n, k = map(int, input().split()) #n:수빈 현재위치 k:동생 현재위치
bfs(n)
print(_list[k])