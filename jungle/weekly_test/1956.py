import sys

def input():
    return sys.stdin.readline().rstrip()

# 단방향 그래프
inf = int(1e9)
v, e = map(int, input().split()) #v개의 마을(1~v), e개의 도로

# 도로를 따라 운동을 하기 위한 경로 찾기. cycle을 찾아야 함. 사이클을 이루는 도로의 길이의 합이 최소.
# 도로 길이의 합이 가장 작은 사이클을 찾는 프로그램 작성.
graph = [[inf] * (v + 1) for _ in range(v + 1)]
for i in range(1,v+1):
    for j in range(1, v+1):
        if i == j:
            graph[i][j] = 0

for _ in range(e):
    st, en, dist = map(int, input().split())
    graph[st][en] = dist

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

min_val = inf
for i in range(1, v+1):
    for j in range(1, v+1):
        if i == j: # 같은 마을로 가는 경우는 제외
            continue
        min_val = min(min_val, graph[i][j] + graph[j][i])

if min_val == inf:
    print(-1)
else:
    print(min_val)