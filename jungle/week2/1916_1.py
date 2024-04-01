import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
# A -> B 도시로 가는데 드는 버스 비용을 최소화.
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    st, en, weight = map(int, input().split())
    adj_list[st].append((en, weight))

start_city, end_city = map(int, input().split())

# 최단 거리를 저장하는 리스트 초기화
dest = [-1]*(N+1)
# 방문 여부를 체크하는 리스트 초기화
vis = [False]*(N+1)

# 시작 도시부터의 최단 거리를 저장하는 우선순위 큐 초기화
pq = [(0, start_city)] # (거리, 도시) 형태의 튜플을 저장
dest[start_city] = 0

# 다익스트라 알고리즘 수행
while pq:
    cur_dist, cur_city = heapq.heappop(pq)
    if vis[cur_city]:
        continue
    vis[cur_city] = True
    for nxt, weight in adj_list[cur_city]:
        # 만약 다음 노드를 아직 방문하지 않았거나,
        # 현재까지의 최단 거리에 현재 노드를 거쳐서 가는 거리가 더 짧다면 최단 거리 갱신
        if not vis[nxt] and (dest[nxt] == -1 or dest[nxt] > cur_dist + weight):
            dest[nxt] = cur_dist + weight
            heapq.heappush(pq, (dest[nxt], nxt))

# 도착 도시까지의 최단 거리 출력
print(dest[end_city])

