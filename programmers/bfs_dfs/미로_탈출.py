from collections import deque
from copy import deepcopy

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# S -> L 또는 L -> E로 이동하는 최단 거리
def bfs(x, y, target, count_map, graph):
    queue = deque()
    count_map[x][y] = 0
    queue.append([x, y])

    while queue:
        curX, curY = queue.popleft()
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if 0 <= nx < len(count_map) and 0 <= ny < len(count_map[0]):
                if count_map[nx][ny] == -1:
                    if graph[nx][ny] == 'O' or graph[nx][ny] == target:
                        count_map[nx][ny] = count_map[curX][curY] + 1
                        if graph[nx][ny] == target:
                            return count_map[nx][ny]
                        queue.append([nx, ny])
    return -1

# 미로를 탈출하는데 필요한 최소시간 return
def solution(maps):

    count_map = [[-1] * len(maps[0]) for _ in range(len(maps))]
    graph = [[] for _ in range(len(maps))]
    x, y = -1, -1  # 시작
    lx, ly = -1, -1  # 레버 좌표

    for idx, lis in enumerate(maps):  # 값 초기화
        for j in range(len(maps[0])):
            if lis[j] == 'S':
                x = idx
                y = j
            if lis[j] == 'L':
                lx = idx
                ly = j
            graph[idx].append(lis[j])

    # S -> L의 최단 거리
    dist_to_l = bfs(x, y, 'L', deepcopy(count_map), graph)
    if dist_to_l == -1:
        return -1

    # L -> E의 최단 거리
    dist_to_e = bfs(lx, ly, 'E', deepcopy(count_map), graph)
    if dist_to_e == -1:
        return -1

    # 전체 최단 거리
    return dist_to_l + dist_to_e

# 테스트
print(solution(["SELXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"]))
