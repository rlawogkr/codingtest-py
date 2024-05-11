import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
# 한 칸에는 아기상어 1마리

dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,-1,1]

dq = deque()
#init
for i in range(n):
    for j in range(m):
        if _map[i][j] == 1:
            dq.append((i,j))
            visited[i][j] = True

def bfs():
    while dq:
        (x,y) = dq.popleft()
        for i in range(8):
            nx = x + dx[i] #5
            ny = y + dy[i] #4
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    _map[nx][ny] = _map[x][y] + 1
                    dq.append((nx,ny))

bfs()
max_size = -int(1e9)

for i in range(n):
    for j in range(m):
        max_size = max(max_size, _map[i][j])

print(max_size-1)