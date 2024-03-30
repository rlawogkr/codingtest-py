import sys
from collections import deque

input = sys.stdin.readline


dq = deque()

# N: 정점의 개수, M: 간선의 개수, V: 탐색 시작 정점
# 간선은 양방향
# [[], [2, 3, 4], [4], [4], []]
N, M, V = map(int, input().rstrip().split()) 
adj_list = [[] for _ in range(N+1)] #0번은 제외

#adj_list 세팅
for _ in range(1, M+1):
    st, en = map(int, input().rstrip().split())
    adj_list[st].append(en)
    adj_list[en].append(st)


# print(adj_list)
# 재귀로 구현
res_dfs = []
visited = [False] * (N+1)
def dfs(v):
    visited[v] = True
    res_dfs.append(v)
    for i in sorted(adj_list[v]):
        if not visited[i]:
            dfs(i)

# V로부터 방문된 점을 순서대로 출력. 정점번호가 작은 것부터 먼저 방문
res_bfs = []
def bfs(V):
    dq = deque()
    visited = [False] * (N+1) 
    visited[V] = True
    dq.append(V)
    #결과값 저장
    res_bfs.append(V)
    while dq:
        tmp = dq.popleft()
        for i in sorted(adj_list[tmp]):
            # 해당 지점을 방문하지 않고, 
            if not visited[i]:
                visited[i] = True
                dq.append(i)
                res_bfs.append(i)

dfs(V)
bfs(V)
print(" ".join(map(str, res_dfs)))
print(" ".join(map(str, res_bfs)))
