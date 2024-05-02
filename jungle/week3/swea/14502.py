import sys
from collections import deque
import copy


def input():
    return sys.stdin.readline().rstrip()


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
_max = -1e9


# 벽 3개 세우기
def solution(cnt):
    global _max, graph
    if cnt == 3:  # 벽을 3개 세웠을 때 bfs 탐색.
        cnt_add = bfs()
        # 0의 개수 세기
        tmp = N*M - cnt_first - cnt_add - 3
        _max = max(_max, tmp)
        return

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                graph[y][x] = 1
                solution(cnt + 1)
                graph[y][x] = 0


# 바이러스 퍼지는 bfs
def bfs():
    ret = 0
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    # 바이러스가 있는 모든 지점 queue에 넣기
    for i, j in virus:
        queue.append((i, j))
        visited[i][j] = True

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (
                0 <= ny < N
                and 0 <= nx < M
                and not visited[ny][nx]
                and graph[ny][nx] == 0
            ):
                visited[ny][nx] = True
                queue.append((ny, nx))
                ret += 1
    return ret


N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]

# 바이러스가 있는 좌표 저장.
virus = []
cnt_first = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i, j))
            cnt_first += 1
        elif graph[i][j] == 1:
            cnt_first += 1
        

solution(0)

print(_max)
