import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

#도시의 개수: N, 도로의 개수: M, 거리정보: K, 출발도시 번호: X
N, M, K, X = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    st, en = map(int, input().split())
    adj_list[st].append(en)
distances = [-1]*(N+1)
distances[X] = 0 #시작점

dq = deque()
dq.append(X)
while dq:
    cur_city = dq.popleft()
    for nxt in adj_list[cur_city]:
        if distances[nxt] == -1:
            distances[nxt] = distances[cur_city] + 1
            dq.append(nxt)

res = []
for idx, distance in enumerate(distances):
    if distance == K:
        res.append(idx)

if not res:
    print(-1)
else:
    print("\n".join(map(str, res)))
