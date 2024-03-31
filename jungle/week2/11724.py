import sys
from collections import deque
input = sys.stdin.readline

#n: 정점의 개수, m: 간선의 개수
n, m = map(int, input().rstrip().split())
#adj_list 초기화
adj_list = [[] for _ in range(1+n)]
for _ in range(m):
 v1, v2 = map(int, input().split())
 adj_list[v1].append(v2)
 adj_list[v2].append(v1)

vis = [False] *(n+1)
def bfs(idx):
    dq = deque()
    dq.append(idx)
    vis[idx] = True
    
    while dq:
       a = dq.popleft()
       for i in adj_list[a]:
          if not vis[i]:
            dq.append(i)
            vis[i] = True

cnt = 0
for i in range(1,n+1):
    if not vis[i]:
        bfs(i)
        cnt += 1

print(cnt)