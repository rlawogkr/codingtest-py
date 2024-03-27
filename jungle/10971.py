import sys
input = sys.stdin.readline
N = int(input().rstrip())
W = []
for _ in range(N):
    _arr = list(map(int, input().rstrip().split()))
    W.append(_arr)

visited = []
_min = sys.maxsize
def dfs(st, en, cost, visited):
    global _min
    if len(visited) == N:
        if W[en][st]:
            _min = min(_min, cost + W[en][st])
        return
    
    for i in range(N):
        if W[en][i] and i not in visited:
            visited.append(i)
            dfs(st, i, cost + W[en][i], visited)
            visited.pop()

for i in range(N):
    dfs(i,i,0,[i])
print(_min)

