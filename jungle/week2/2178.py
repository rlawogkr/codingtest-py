import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
dy = [0,1,0,-1]
dx = [1,0,-1,0]
maze = [[] for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in input():
        maze[i].append(int(j))



def bfs(x,y):
    global maze
    q = deque()
    q.append((y,x))
    visited[y][x] = True

    while q:
        y,x = q.popleft()
        
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0<=new_x<m and 0<=new_y<n and maze[new_y][new_x] != 0 and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                maze[new_y][new_x] = maze[y][x] + 1
                q.append((new_y, new_x))

bfs(0,0)
print(maze[n-1][m-1])