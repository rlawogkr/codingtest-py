import sys
#16929. Two Dots
#같은 색으로 이루어진 사이클이 존재하는지 확인
def input():
    return sys.stdin.readline().rstrip()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n, m = map(int, input().split()) # n: row, m: column
graph = [list(input()) for _ in range(n)]

def dfs(x, y, px, py, color): #px, py: 이전 좌표
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == color:
            if not visited[nx][ny]:
                if dfs(nx, ny, x, y, color):
                    return True
            elif visited[nx][ny] and (nx != px or ny != py):
                return True
    return False

for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        if dfs(i, j, -1, -1, graph[i][j]):
            print("Yes")
            sys.exit()
print("No")

#prev_x, prev_y: 이전 좌표
# def dfs(x, y, prev_x, prev_y, color):
#     visited[x][y] = True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == color:
#             if not visited[nx][ny]:
#                 if dfs(nx, ny, x, y, color):
#                     return True
#             # 이전 좌표로 되돌아가는 경우
#             elif visited[nx][ny] and (nx != prev_x or ny != prev_y):
#                 return True
#     return False
