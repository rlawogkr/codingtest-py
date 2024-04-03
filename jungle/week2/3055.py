from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
distance = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()

def bfs(dest_y, dest_x):
    while queue:
        cur_y, cur_x = queue.popleft()
        # 도착 지점 확인
        if cur_y == dest_y and cur_x == dest_x:
            return distance[dest_y][dest_x]
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                # 물이 차있는 곳으로 이동할 수 없음
                if (graph[ny][nx] == '.' or graph[ny][nx] == 'D') and graph[cur_y][cur_x] == 'S':
                    graph[ny][nx] = 'S'
                    distance[ny][nx] = distance[cur_y][cur_x] + 1
                    queue.append((ny, nx))
                # 고슴도치가 있어도 물로 수장시킴
                elif (graph[ny][nx] == '.' or graph[ny][nx] == 'S') and graph[cur_y][cur_x] == '*':
                    graph[ny][nx] = '*'
                    queue.append((ny, nx))
    return "KAKTUS"


for y in range(n):
    for x in range(m):
        # 시작 지점
        if graph[y][x] == 'S':
            queue.append((y, x))
        # 도착 지점
        elif graph[y][x] == 'D':
            dst_y, dst_x = y, x

# 물 차는 지점을 먼저 queue에 넣어줌
for y in range(n):
    for x in range(m):
        if graph[y][x] == '*':
            queue.append((y, x))

print(bfs(dst_y, dst_x))
