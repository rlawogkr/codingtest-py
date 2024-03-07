import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    
    while dq:
        _tuple = dq.popleft()
        x, y = _tuple[0], _tuple[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    dq.append((nx, ny))

dx = [1, 0, -1, 0] # 우, 하, 좌, 상
dy = [0, 1, 0, -1]

testcase = int(input())
res = []

for _ in range(testcase):
    m, n, k = map(int, input().split()) # m:가로 n:세로 k:배추 심어진 위치 개수
    graph = [[0 for i in range(m)] for j in range(n)]
    
    # 그래프 초기화
    for _ in range(k):
        y,x = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)