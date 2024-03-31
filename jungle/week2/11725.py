import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip()) #노드의 갯수
adj_list = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().rstrip().split())
    adj_list[x].append(y)
    adj_list[y].append(x)
# print(adj_list)

vis = [False] * (n+1)
parent_node = [0] * n # 1개씩 뺀다고 생각. 0부터 시작. 
def bfs(idx):
    dq = deque()
    vis[idx] = True
    dq.append(idx)
    while dq:
        a = dq.popleft()
        for i in adj_list[a]:
            if not vis[i]:
                vis[i] = True
                parent_node[i-1] = a
                dq.append(i)

for i in range(1, n+1):
    if vis[i]: continue
    else:
        bfs(i)

print("\n".join(map(str, parent_node[1:n])))
