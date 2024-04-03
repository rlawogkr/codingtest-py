import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

#M:가로 N:세로 H:쌓아올린 상자 수
M, N, H = map(int, input().split())

tomatoes = [[[-2]*M for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        tomatoes[i][j] = list(map(int, input().split()))

dx = [1,0,-1,0]
dy = [0,1, 0, -1]
dz = [1,-1]

def bfs():
    global tomatoes
    dq = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] == 1: #익은 토마토 전부 때려넣음
                    dq.append((i,j,k))
    
    while dq:
        z,y,x = dq.popleft()
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0<=new_x<M and 0<=new_y<N and tomatoes[z][new_y][new_x] == 0:
                tomatoes[z][new_y][new_x] = tomatoes[z][y][x] + 1
                dq.append((z,new_y,new_x))
        for i in range(2):
            new_z = z + dz[i]
            if 0<=new_z<H and tomatoes[new_z][y][x] == 0:
                tomatoes[new_z][y][x] = tomatoes[z][y][x] + 1
                dq.append((new_z,y,x))

bfs()
max_day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 0:
                print(-1)
                sys.exit()
            max_day = max(max_day, tomatoes[i][j][k])
print(max_day-1)