#단지 번호 붙이기
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
apt = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    count = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and apt[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                count += 1
                q.append((ny,nx))
    return count

answer = []
for i in range(N):
    for j in range(N):
        if apt[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i,j))

answer.sort()
print(len(answer))
print("\n".join(map(str,answer)))