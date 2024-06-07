
# 16940. BFS 스페셜 저지

from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)] # bfs 시 탐색 여부 확인을 위함
children = [set() for _ in range(N+1)] # 트리의 부모자식 관계를 알기 위함

for _ in range(N-1): # 그래프 생성
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# [1,2,3,4] or [1,3,2,4]
order = list(map(int, input().split())) # 비교할 탐색 루트

# bfs