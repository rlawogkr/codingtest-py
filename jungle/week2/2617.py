# 구슬 찾기
# 2617

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heavy = [[] for _ in range(N + 1)]
light = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    heavy[a].append(b)
    light[b].append(a)

def dfs(list, root):
    count = 0
    for i in list[root]:# list[root] = root와 연결된 노드들
        if not visited[i]:
            visited[i] = True
            count += 1 # 연결된 노드의 수를 세줌
            count += dfs(list, i) # 재귀적으로 연결된 노드들을 탐색
    return count 

mid = (N + 1) // 2
res = 0

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    if dfs(heavy, i) >= mid:
        res += 1
    elif dfs(light, i) >= mid:
        res += 1
print(res)