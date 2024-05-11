import sys
from itertools import combinations

#15686. 치킨배달
def input():
    return sys.stdin.readline().rstrip()
'''
치킨거리? 집과 가장 가까운 치킨집 사이의 거리. 
각각의 집은 치킨 거리를 가지고 있음.
0: 빈칸 1: 집 2: 치킨집
도시에 있는 치킨집 중 최대 M개를 고르고, 나머지 치킨집은 폐업.
어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하기
폐업시키지 않을 치킨 집을 최대 M개 골랐을 때, 도시의 치킨 거리의 최솟값?
'''
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
result = int(1e9)
for comb in combinations(chicken, m):
    sum = 0

    for x, y in dest: # 도시의 거리
        min_dist = int(1e9)
        for cx, cy in comb:
            min_dist = min(min_dist, abs(x-cx) + abs(y-cy))
        sum += min_dist
    result = min(result, sum)

print(result)

