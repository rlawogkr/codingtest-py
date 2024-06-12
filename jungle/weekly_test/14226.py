#14226. 이모티콘
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def bfs():
    q = deque()
    q.append((1,0)) # screen emoji 수, clipboard emoji 수
    visited[1][0] = 0
    while q:
        s, c = q.popleft()
        if s == S:
            return visited[s][c]
        # 복사
        if 0 < s <= 1000 and not visited[s][s]:
            visited[s][s] = visited[s][c] + 1
            q.append((s,s))
        # 붙여넣기
        if s+c <= 1000 and not visited[s+c][c]:
            visited[s+c][c] = visited[s][c] + 1
            q.append((s+c,c))
        # 삭제
        if s-1 >= 0 and not visited[s-1][c]:
            visited[s-1][c] = visited[s][c] + 1
            q.append((s-1,c))

S = int(input())
visited = [[False]*1001 for _ in range(1001)]
print(bfs())
