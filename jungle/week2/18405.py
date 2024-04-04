#경쟁적 전염
#매 초마다 번호가 낮은 종류의 바이러스부터 증식
#s초가 지난 후 (x,y)에 존재하는 바이러스의 종류를 출력
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx = [1,0,-1,0]
dy = [0,1,0,-1]
N, K = map(int, input().split()) #N*N 시험관, K종류 바이러스
_map = [list(map(int, input().split())) for _ in range(N)]
S, Y, X = map(int, input().split()) #S초 후, Y, X 좌표
q = deque()
for i in range(N):
    for j in range(N):
        if _map[i][j] != 0:
            q.append((_map[i][j], i, j, 0))
q = deque(sorted(q, key = lambda x: x[0])) # 번호가 낮은 바이러스부터 증식 
# print(q)

while q:
    virus, y, x, time = q.popleft()
    if time == S:
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and _map[ny][nx] == 0:
            _map[ny][nx] = virus
            q.append((virus, ny, nx, time + 1))
print(_map[Y - 1][X - 1])