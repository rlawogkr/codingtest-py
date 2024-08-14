import sys

#1799. 비숍
dx = [-1,-1,1,1]
dy = [-1,1,-1,1]
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
# 1: 비숍을 놓을 수 있는 칸, 0: 비숍을 놓을 수 없는 칸
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# (x,y) 위치에 비숍을 놓을 수 있는지 확인
def check(x, y):
    for i in range(4):
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
            if visited[nx][ny]:
                return False
    return True



def dfs(x, y, cnt):
    global answer
    # 다음 row 으로 이동. 첫 col 부터 시작
    if y == n:
        x += 1
        y = 0
    if x == n:
        answer = max(answer, cnt)
        return

    if board[x][y] == 1 and check(x, y):
        visited[x][y] = True
        dfs(x, y+1, cnt+1)
        visited[x][y] = False
    dfs(x, y+1, cnt)

answer = 0
dfs(0,0,0)
print(answer)