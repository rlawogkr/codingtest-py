import sys
from collections import deque

input = sys.stdin.readline

# 물에 잠기지 않는 안전한 영역의 최대 개수를 계산
# 물이 1일 경우 ~ 물이 max(_location)인 경우까지
dx = [1, 0, -1, 0] #우, 하, 좌, 상
dy = [0, 1, 0, -1]

#water보다 작은 값은 count하지 않음.
def bfs(y, x, water):
    dq = deque()
    dq.append(y)
    dq.append(x)

    while dq:
        a = dq.popleft() #y좌표
        b = dq.popleft() #x좌표
        for i in range(4):
            new_a = a + dy[i] #y좌표
            new_b = b + dx[i] #x좌표
            if new_a >= 0 and new_a < n and new_b >= 0 and new_b < n:
                if _location[new_a][new_b] > water and not _visited[new_a][new_b]:
                    _visited[new_a][new_b] = True
                    dq.append(new_a)
                    dq.append(new_b)


n = int(input().rstrip()) #2차원 배열의 행과 열의 개수
_location = [list(map(int, input().split())) for _ in range(n)]

#가장 높은 위치
high_loc = 0
for row in _location:
    if high_loc < max(row): high_loc = max(row)



_max = -sys.maxsize #최대값일 경우에만 갱신

for water in range(high_loc+1):
    _visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n): #y좌표
        for j in range(n): #x좌표
            if _location[i][j] > water and not _visited[i][j]: #설정을 안하면 모든 지점을 다 돌리게 된다.
                bfs(i,j,water)
                cnt += 1
    if cnt >= _max: _max = cnt


print(_max)