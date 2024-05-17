import sys
from itertools import combinations

#15686. 치킨배달
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split()) # 크기가 n*n
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

chicken = [] # 치킨집이 있는 곳
dest = [] # 목적지. 집이 있는 곳
# 도시의 치킨 거리? 모든 집의 치킨 거리의 합.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2: # 치킨집
            chicken.append((i,j))
        elif graph[i][j] == 1: # 도시
            dest.append((i,j))

# 치킨집 중에서 m개를 고르는 모든 경우의 수
# 도시의 치킨 거리? 모든 집의 치킨 거리의 합
result = int(1e9)
for comb in combinations(chicken, m):
    sum = 0
    for x,y in dest:
        min_dist = int(1e9)
        for cx, cy in comb:
            min_dist = min(min_dist,abs(x - cx) + abs(y - cy))
        sum += min_dist

result = min(sum, result)
print(result)
