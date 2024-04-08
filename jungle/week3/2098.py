import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input()) #도시의 수

graph = [list(map(int, input().split())) for _ in range(N)]

#가장 적은 비용을 들이는 외판원의 순회 경로.
min_val = sys.maxsize
visited = []
def dfs(st, en, cost, visited):
    global min_val
    if len(visited) == N:
        if graph[en][st]:
            min_val = min(min_val, cost + graph[en][st])
        return
    
    for i in range(N):
        if graph[en][i] and i not in visited:
            visited.append(i)
            dfs(st, i, cost + graph[en][i], visited)
            visited.pop()

for i in range(N):
    dfs(i,i,0,[i])


