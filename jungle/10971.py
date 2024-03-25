import sys

input = sys.stdin.readline

n = int(input().rstrip())

_list = [[0]*n for _ in range(n)]
_visited = []
_min = sys.maxsize

#시작 지점, 끝 지점, 더해가는 거리(깊이에 따라 값을 더해갈 예정)
def dfs(st, dest, weight, _visited):
    global _min
    if len(_visited) == n:
        if _list[dest][st]: 
            _min = min(_min, weight + _list[dest][st])
            return
    
    for i in range(n):
        if _list[dest][i] and i not in _visited and weight < _min:
            _visited.append(i)
            dfs(st,i,weight + _list[dest][i], _visited)
            _visited.pop()

#값 입력
for i in range(n):
    for j,val in enumerate(map(int, input().rstrip().split())):
        _list[i][j] = val

for i in range(n):
    dfs(i,i,0,[i])

print(_min)
