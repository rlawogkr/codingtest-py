import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

# m: row, n: col, k개의 직사각형을 그림
m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
for _ in range(k):
    # (x1,y1), (x2,y2)의 좌표. 왼쪽 아래, 오른쪽 위
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def dfs(x,y):
    visited[x][y] = True
    area = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
            if not visited[nx][ny]:
                area += dfs(nx, ny)
    return area
def bfs(x,y): #(x,y)는 시작점
    visited[x][y] = True
    dq = deque()
    dq.append((x,y))

    area = 1 # 사각형 넓이
    while dq:
        (x,y) = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append((nx,ny))
                    area += 1
    return area

cnt = 0
area_list = []
for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 0:
            cnt += 1
            area_list.append(dfs(i,j))

area_list.sort()
print(cnt)
print(' '.join(map(str, area_list)))
