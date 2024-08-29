import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx = [-1,0,1,0] # 상, 우, 하, 좌
dy = [0,1,0,-1]

c, r = map(int, input().split())
graph = [[] for _ in range(r)]
visited = [[-1]*c for _ in range(r)]

for i in range(r):
    tmp = input()
    for j in range(c):
        graph[i].append(tmp[j])

# 벽을 최소 몇 개를 부셔야 하는지? bfs 로 접근
def bfs():
    dq = deque([(0,0)])
    visited[0][0] = 0 # 방문 처리

    while dq:
        curx, cury = dq.popleft()
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0<=nx<r and 0<=ny<c and visited[nx][ny] == -1:
                if graph[nx][ny] == '0':
                    visited[nx][ny] = visited[curx][cury] # 벽을 부술 필요가 없음
                    dq.appendleft((nx,ny)) # 우선적으로 처리
                elif graph[nx][ny] == '1':
                    visited[nx][ny] = visited[curx][cury] + 1
                    dq.append((nx,ny)) # 나중에 처리


bfs()
print(visited[r-1][c-1])