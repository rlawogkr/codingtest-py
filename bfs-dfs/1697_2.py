from collections import deque

def bfs(start, target):
    visited = [False] * 100001
    queue = deque([(start, 0)])  # (현재 위치, 이동 횟수)

    while queue:
        current_pos, count = queue.popleft()

        if current_pos == target:
            return count

        for next_pos in (current_pos - 1, current_pos + 1, current_pos * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, count + 1))

# 입력 받기
n, k = map(int, input().split())

# BFS 수행
result = bfs(n, k)
print(result)
