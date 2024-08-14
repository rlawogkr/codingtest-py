import sys
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()

n = int(input())  # 물건의 개수 (1 ~ n)
m = int(input())  # 미리 측정된 물건 쌍의 개수

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

for _ in range(m):
    st, en = map(int, input().split())
    graph[st].append(en)
    reverse_graph[en].append(st)

def dfs(graph, v):
    count = 1
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            count += dfs(graph, node, visited)
    return count

for i in range(1, n+1):
    visited = [False] * (n+1)
    count1 = dfs(graph, i, visited) - 1  # 시작점 제외

    visited = [False] * (n+1)
    count2 = dfs(reverse_graph, i, visited) - 1  # 시작점 제외

    # 전체 개수에서 도달할 수 있는 개수와 도달할 수 없는 개수를 빼준다
    print(n - (count1 + count2 + 1))
