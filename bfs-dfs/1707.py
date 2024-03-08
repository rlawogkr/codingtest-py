from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()

def bfs(x):
    dq = deque()
    dq.append(x)
    visited[x] = 5

    while dq:
        val = dq.popleft()
        
        for i in graph[val]:
            if visited[i] == 0:
                visited[i] = -visited[val]
                dq.append(i)
            elif visited[i] == visited[val]:
                return False
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split()) # v:정점의 개수, e:간선의 개수
    graph = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    
    #인접 리스트 초기화
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    


    #bfs
    flag = True
    for i in range(1, v+1):
        if visited[i] == 0:
            dq = deque()
            dq.append(i)
            visited[i] = 5 # 임의의 값으로 방문표시
            while dq:
                val = dq.popleft()
                for j in graph[val]:
                    if visited[j] == 0:
                        visited[j] = -visited[val]
                        dq.append(j)
                    elif visited[j] == visited[val]:
                        flag = False
                        break
    
    print(visited)
    if flag == True:
        print("YES")
    else:
        print("NO")