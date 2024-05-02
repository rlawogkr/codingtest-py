import sys
import heapq
import copy
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
INF = 1e9
def dijkstra(graph, start):
    # 각 컴퓨터가 감염되기까지 걸리는 최단 시간을 기록하는 리스트
    time = [INF] * (len(graph))
    time[start] = 0

    # 감염되는 컴퓨터의 개수, 마지막 컴퓨터가 감염되기까지 걸리는 시간
    count, endTime = 0, 0

    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        cur_time, cur_computer = heapq.heappop(pq)
        if cur_time < time[cur_computer]:
            continue

        for next in graph[cur_computer]:
            next_time, next_computer = next[0], next[1]
            # 최단 시간 갱신
            if cur_time + next_time < time[next_computer]:
                time[next_computer] = cur_time + next_time
                heapq.heappush(pq, (cur_time + next_time, next_computer))


    for t in time:
        if t < INF:
            count +=1
            # 마지막 컴퓨터가 감염되는 시간
            if t > endTime:
                endTime = t

    return count, endTime



for _ in range(T):
    num, dependency, c = map(int, input().split()) #컴퓨터 갯수, 의존성 갯수, 해킹당한 컴퓨터 번호
    graph = [[] for _ in range(num+1)]

    for _ in range(dependency):
        # 단방향
        a, b, s = map(int, input().split()) # b -> a, s초 후 컴퓨터 a도 감염
        graph[b].append((s,a))
        '''
        [[], [(2, 5)], [(3, 5)], []]
        [[], [(2, 2), (3, 8)], [(3, 4)], []]
        '''
    count, end_time = dijkstra(graph, c)
    print(count, end_time)

