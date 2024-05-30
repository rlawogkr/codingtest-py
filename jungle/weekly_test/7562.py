import sys
from collections import deque
#7562. 나이트의 이동
def input():
    return sys.stdin.readline().rstrip()

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            return visited[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

for _ in range(int(input())):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    print(bfs(start_x, start_y))

