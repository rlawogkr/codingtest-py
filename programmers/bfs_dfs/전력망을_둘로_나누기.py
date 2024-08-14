from collections import deque

def bfs(start, graph, visited, n):
    dq = deque([start])
    visited[start] = True
    count = 1  # 현재 노드의 개수

    while dq:
        node = dq.popleft()

        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                dq.append(next)
                count += 1

    return abs(n - 2 * count)

def solution(n, wires):
    answer = 1e9  # 큰 값으로 초기화

    for i in range(len(wires)):
        # 그래프 생성
        graph = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)

        print(graph)

        # 방문 배열 초기화 및 dfs 호출
        visited = [False] * (n + 1)
        # 임의의 시작 노드로 dfs 호출
        diff = bfs(2, graph, visited, n)

        # 최소 차이 갱신
        answer = min(answer, diff)

    return answer
