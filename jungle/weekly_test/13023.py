import sys
# 13023. ABCDE
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split()) #n: 사람의 수, m: 친구 관계의 수

adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def dfs(cur, cnt):
    if cnt == 4:
        print(1)
        exit()
    for next in adj_list[cur]:
        if not visited[next]:
            visited[next] = True
            dfs(next, cnt+1)
            visited[next] = False

visited = [False] * (n+1)
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
print(0)