import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 처음 좌표(r,c). d: 방향(상, 우, 하, 좌)

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1, 0, 1, 0] # 상0, 우1, 하2, 좌3
dy = [0, 1, 0, -1]


def cleanUp(r, c, d):
    cnt = 0

    while True:
        if not visited[r][c]:
            visited[r][c] = True
            cnt += 1

        flag = False
        for _ in range(4):
            d = (d + 3) % 4 # 반시계 방향 회전
            nx = r + dx[d]
            ny = c + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
                r, c = nx, ny # r, c 업데이트
                flag = True
                break

        if not flag: # 4방향 모두 청소가 되었거나 벽인 경우
            nx = r - dx[d]
            ny = c - dy[d]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1: # 후진
                r, c = nx, ny # r, c 업데이트
            else:
                break

    return cnt

print(cleanUp(r, c, d))
