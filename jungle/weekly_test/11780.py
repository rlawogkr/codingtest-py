import sys

input = sys.stdin.readline

INF = 1e9
n = int(input()) #도시
m = int(input()) #한 도시에서 다른 도시에 도착
#모든 도시의 쌍에 대해 A->B로 가는데 필요한 비용 최소값
#Floyd-Warshall
#외부에 padding 설정
graph = [[INF]*(n+1) for _ in range(n+1)]
path = [[[i] for i in range(n+1)] for i in range(n+1)]

#그래프 초기화
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(graph[a][b], cost)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            if graph[i][j] > graph[i][k] + graph[k][j]: # k를 거쳐가는 것이 더 빠를 경우에
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                path[i][j] = path[i][k] + path[k][j] # i->k->j로 가는 경로

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
# i -> j 경로
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0)
        else:
            # i에서 j로 가는 경로의 길이와 경로 출력
            print(len(path[i][j])+1, i, *path[i][j])

'''
[[[0], [1], [2], [3], [4], [5]], 
[[0], [1], [2], [3], [4], [3, 5]], 
[[0], [4, 5, 1], [2], [4, 5, 1, 3], [4], [4, 5]], 
[[0], [1], [5, 2], [3], [4], [5]], 
[[0], [5, 1], [5, 2], [5, 1, 3], [4], [5]], 
[[0], [1], [2], [1, 3], [2, 4], [5]]]
'''

