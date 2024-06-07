import sys
from collections import deque
from copy import deepcopy
#16947. 서울 지하철 2호선
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, prev):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            if dfs(i, x):
                return True
        elif visited[i] and i != prev:
            cycle.append(i)
            return True
    return False

visited = [False] * (n+1)
cycle = []
dfs(1, 0)
visited = [False] * (n+1)
for i in cycle:
    visited[i] = True

def bfs(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)

for i in cycle:
    visited[i] = 1
    bfs(i)
    visited[i] = 0

print(*visited[1:])