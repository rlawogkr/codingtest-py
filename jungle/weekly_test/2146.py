# 2146. 다리 만들기
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
num = 1 # 섬 번호
res = int(1e9)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 1번째 bfs (섬 구분)
def bfs1(i, j):
  que = deque()
  que.append([i,j])
  while que:
    x, y = que.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      # 범위 안, 방문 안한 곳, 섬
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny]:
        visited[nx][ny] = 1
        graph[nx][ny] = num
        que.append([nx,ny])

        
# 2번째 bfs (최단거리 구하기)
def bfs2(cur):
  queue = deque()
  dist = [[-1]*n for _ in range(n)] # 거리

  for i in range(n):
    for j in range(n):
      if graph[i][j]==cur: # 현재 섬
        dist[i][j] = 0
        queue.append([i,j])

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<n and 0<=ny<n:
        # 다른 섬 만남. 연결됐을 경우
        if graph[nx][ny] and graph[nx][ny]!=cur: # v? 현재 섬
          return dist[x][y]
        # 물이고 아직 다리 없는 곳
        elif not graph[nx][ny] and dist[nx][ny]==-1:
          dist[nx][ny] = dist[x][y]+1
          queue.append([nx,ny])
  return int(1e9)



'''
[1, 1, 1, 0, 0, 0, 0, 2, 2, 2], 
[1, 1, 1, 1, 0, 0, 0, 0, 2, 2], 
[1, 0, 1, 1, 0, 0, 0, 0, 2, 2], 
[0, 0, 1, 1, 1, 0, 0, 0, 0, 2], 
[0, 0, 0, 1, 0, 0, 0, 0, 0, 2], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 3, 3, 0, 0, 0, 0], 
[0, 0, 0, 0, 3, 3, 3, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''
# 섬 구분
for i in range(n):
  for j in range(n):
    if graph[i][j] and not visited[i][j]:
      visited[i][j] = 1
      graph[i][j] = num
      bfs1(i, j)
      num += 1


# 최단거리 구하기
for v in range(1,num):
  res = min(res, bfs2(v))
print(res)
