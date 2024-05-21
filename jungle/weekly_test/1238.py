import sys
from heapq import heappop, heappush
# 1238. 파티
def input():
    return sys.stdin.readline().rstrip()

inf = int(1e9)
n, m, x = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    st, en, cost = map(int, input().split())
    adj_list[st].append((cost, en))

def dijkstra(st):
    heap = []
    dist = [inf] * (n+1)
    dist[st] = 0
    heappush(heap, (0, st))

    while heap:
        cost, cur = heappop(heap)
        for next_cost, next_cur in adj_list[cur]:
            if next_cost + cost < dist[next_cur]:
                dist[next_cur] = next_cost + cost
                # 해주는 이유? 다음 노드로 가는 비용이 더 작을 경우 갱신해주기 위함
                heappush(heap, (next_cost + cost, next_cur))
    return dist




dist = dijkstra(x) # x에서 모든 지점으로 가는 최단거리
ans = 0
for i in range(1, n+1):
    if i == x:
        continue
    go = dijkstra(i) # i에서 x로 가는 최단거리
    ans = max(ans, dist[i] + go[x])
print(ans)

'''
def dijkstra(start):
    dist = [inf] * (n+1)
    dist[start] = 0
    heap = []
    heappush(heap, (0, start))
    while heap:
        cost, st = heappop(heap)
        if dist[st] < cost:
            continue
        for next_cost, next_node in adj_list[st]:
            next_cost += cost
            if next_cost < dist[next_node]:
                dist[next_node] = next_cost
                heappush(heap, (next_cost, next_node))
    return dist
'''