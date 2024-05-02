import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 두 사람 번호
m = int(input()) # 서로 다른 두 사람의 관계의 갯수

# 두 사람의 친척 관계가 없을 경우 -1
# dfs
adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    st, en = map(int, input().split())
    adj_list[st].append(en)
    adj_list[en].append(st)

visited = [False] * (n+1)
distance = [0] * (n+1)
def bfs(st, en):
    dq = deque()
    dq.append(st)
    visited[st] = True
    distance[st] = 0

    while dq:
        a = dq.popleft()

        for i in adj_list[a]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)
                distance[i] = distance[a] + 1

    if distance[en] == 0:
        return -1
    return distance[en]

print(bfs(a, b))



