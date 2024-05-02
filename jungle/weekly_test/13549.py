import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

# st: 현재 점 위치(수빈)
# en: 동생 위치
st, en = map(int, input().split())
INF = int(1e9)
dist = [1e9] * 100001

def move(i, cost, node):
    if i == 0:
        return (cost + 1,node -1)
    elif i == 1:
        return (cost + 1, node +1)
    else:
        return (cost, 2 * node)
def dijkstra(st): # Greedy. 항상 최소의 위치만 선택.
    dist[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))

    while heap:
        (cost, node) = heapq.heappop(heap)
        for i in range(3):
            n_cost, n_node = move(i, cost, node)
            if 0 <= n_node <= 100000 and dist[n_node] > n_cost:
                heapq.heappush(heap, (n_cost, n_node))
                dist[n_node] = n_cost

dijkstra(st)
print(dist[en])


