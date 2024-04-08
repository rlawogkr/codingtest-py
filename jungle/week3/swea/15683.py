import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

#cctv는 방향에 있는 칸 전체를 감시할 수 있음.
#cctv는 벽을 통과할 수 없음.
#0: 빈칸, 6: 벽, 회전: 90도 방향
#1~5: cctv 번호.

#cctv의 방향을 적절히 정해, 사각지대의 최소 크기를 구하기
N, M = map(int, input().split()) #row, col
graph = [list(map(int, input().split())) for _ in range(N)]

total_count = N*M
dy = [0,1,0,-1]
dx = [1,0,-1,0]
dir = 0 # 방향, 90도로 변함.

#좌표값, 방향. 1을 마주쳤을 때.
def bfs_1(i, j, dir):
    q = deque()
    q.append((i,j)) #y,x
    
    while q:
        y, x = q.popleft()
        for k in range(4):
            n_y = y + dy[k]
            n_x = x + dx[k]
            if 0 <= n_x < M and 0<= n_y < N:
                # 감시카메라일때
                if 1 <= graph[n_y][n_x] < 6:
                    q.append((n_y, n_x))
                # 벽일 경우
                elif graph[n_y][n_x] == 6:
                    break
                # 0일 경우
                else:


# for i in N:
#     for j in M:
#         if graph[i][j] == 1:
#             pass
#         elif graph[i][j] == 2:
#             pass
#         elif graph[i][j] == 3:
#             pass
#         elif graph[i][j] == 4:
#             pass
#         elif graph[i][j] == 5:
#             pass