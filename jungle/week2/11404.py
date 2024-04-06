# 플로이드 워셜
import sys

def input():
    return sys.stdin.readline().rstrip()

INF = int(1e9)
n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

_map = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i == j: 
            _map[i][j] = 0

#단방향. 시작도시와 도착도시 연결하는 노선은 하나가 아닐 수 있음.
for _ in range(m):
    st, en, cost = map(int, input().split())
    _map[st][en] = min(_map[st][en], cost)
    

#DP
for k in range(1, n+1): # 거쳐가는 점
    for st in range(1, n+1):
        for en in range(1, n+1):
            _map[st][en] = min(_map[st][en], _map[st][k] + _map[k][en])

for i in range(1, n+1):
    for j in range(1, n+1):
        if _map[i][j] == INF: print(0, end = " ")
        else:
            print(_map[i][j], end = " ")
    print()
