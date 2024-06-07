import sys
def input():
    return sys.stdin.readline().rstrip()
def dfs(cur):
    visited[cur] = True
    for i in graph[cur]:
        if not visited[i]:
            dfs(i)

n = int(input()) # 도시의 개수
m = int(input()) # 여행 계획에 속한 도시의 개수
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(1, n+1):
    arr = list(map(int, input().split())) # 0 1 0
    for j in range(1, n+1):
        if arr[j - 1] == 1:
            graph[i].append(j)

travel_plan = list(map(int, input().split()))
counter = 0

for city in travel_plan:
    if not visited[city]:
        counter += 1
        dfs(city)

if counter == 1:
    print("YES")
else:
    print("NO")
