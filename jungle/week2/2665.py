# 검은 방 몇 개를 흰 방으로 바꿈
# 이 때 되도록 적은 수의 검은 방을 흰 방으로 바꿈.
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


n = int(input())

maze = [[] for _ in range(n)]
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in input():
        maze[i].append(int(j))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dijkstra(x, y):
    global maze
    heap = []
    heapq.heappush(heap, (0, (y, x)))  # (거리, (y,x)). 거리를 중심으로 minheap.
    visited[y][x] = True

    while heap:
        dist, (y, x) = heapq.heappop(heap)
        if y == n - 1 and x == n - 1:
            return dist

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                # 검은 방일 경우 dist + 1
                if maze[new_y][new_x] == 0:
                    heapq.heappush(heap, (dist + 1, (new_y, new_x)))
                # 흰 방일 경우 그냥 dist
                else:
                    heapq.heappush(heap, (dist, (new_y, new_x)))


print(dijkstra(0, 0))
