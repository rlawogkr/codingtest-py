import sys
def input():
    return sys.stdin.readline().rstrip()

# 첫째 열: 빵집의 가스관, 마지막 열: 원웅이 빵집
r, c = map(int, input().split()) # r: row, c: column
graph = [list(input()) for _ in range(r)]
# 오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선
dx = [-1, 0, 1]
dy = [1, 1, 1]
def dfs(x, y):
    if y == c - 1:
        return True
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
            graph[nx][ny] = 'x'
            if dfs(nx, ny):
                return True
    return False

result = 0
for i in range(r):
    if dfs(i, 0):
        result += 1
print(result)