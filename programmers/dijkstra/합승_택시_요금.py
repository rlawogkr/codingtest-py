from heapq import heappush, heappop

def solution(n,s,a,b,fares):
    answer = 1e9
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        start, end, cost = fare
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    def dijkstra(start):
        dist = [INF] * (n+1)
        dist[start] = 0
        q = []
        heappush(q, (0, start))
        while q:
            cost, now = heappop(q)
            if dist[now] < cost:
                continue
            for i in graph[now]:
                new_cost = cost + i[1]
                if new_cost < dist[i[0]]:
                    dist[i[0]] = new_cost
                    heappush(q, (new_cost, i[0]))
        return dist
    dist = [dijkstra(i) for i in range(n+1)]

    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])

    return answer

# Sample Test
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])) # 82