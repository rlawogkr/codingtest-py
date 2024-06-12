# 1800. 인터넷 설치

# 특정 가중치 이하의 간선으로만 경로를 구성할 수 있는가?
# 특정 가중치가 넘는 간선의 경우 1의 가중치를 둠
# 특정 가중치가 넘지 않는 간선의 경우 0의 가중치를 둠

import sys
from heapq import heappush, heappop

def input():
    return sys.stdin.readline().rstrip()

def dijkstra(st, limit):
    heap = [] # 탐색할 경로들을 저장하는 장소
    dist = [INF] * (n + 1) # 각 장소까지 최단 경로를 저장하는 리스트
    heappush(heap, (0, st))
    dist[st] = 0

    while heap:
        cost, node = heappop(heap)
        if dist[node] < cost: # 이미 더 저렴한 비용으로 node에 도달하느 경우는 무시
            continue
        for edge_cost, neighbor in internet[node]: # 다음 위치 탐색
            if edge_cost > limit: # limit보다 큰 edge_cost를 가진 간선의 경우 new_cost에 1의 가중치를 둠
                new_cost = cost + 1
            else: # 특정 가중치가 넘지 않는 간선의 경우 0의 가중치를 둠
                new_cost = cost
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heappush(heap, (new_cost, neighbor))

    return dist[n] <= k

INF = int(1e9)
n, p, k = map(int, input().split())
internet = [[] for _ in range(n + 1)]

for _ in range(p):
    a, b, cost = map(int, input().split())
    internet[a].append((cost, b))
    internet[b].append((cost, a))

left = 0
right = int(1e6)
res = INF

# 이분탐색을 통한 최소 가중치 찾기. 해당 가중치 이하의 비용을 갖는 경로를 탐색
while left <= right:
    mid = (left + right) // 2
    if dijkstra(1, mid):
        res = mid
        right = mid - 1
    else:
        left = mid + 1

if res == INF:
    print(-1)
else:
    print(res)
