import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

INF = int(1e9)
def dijkstra(start):
    heap= []
    heapq.heappush(heap,(0,start)) # (거리, 노드). 거리를 중심으로 minheap.
    distance[start] = 0

    while heap:
        dist, cur = heapq.heappop(heap)

        # 최단거리테이블에 기록된 정보보다 꺼낸 거리가 더 길면 무시
        if distance[cur] < dist:
            continue

        #현재 노드와 연결된 인접 노드 확인
        for nxt, w in adj_list[cur]:
            
            if dist+w < distance[nxt] :
                distance[nxt] = dist+w
                heapq.heappush(heap,(dist+w,nxt))


#V == 5일 때 1~5까지 노드가 있는거임.
V, E = map(int,input().split())

start = int(input()) #시작 노드

adj_list = [[] for _ in range(V+1)]
distance = [INF] * (V+1) #최단 거리 테이블
#연결 정보 입력
for _ in range(E):
    st,en,w = map(int,input().split())
    adj_list[st].append((en,w))


dijkstra(start)

#i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])