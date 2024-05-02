# import sys

# def input():
#     return sys.stdin.readline().rstrip()

dx = [1,0,-1,0]
dy = [0,1, 0, -1]

# 좌표, 현재까지 dist, 공사 했는지 유무
def dfs(y, x, dist, K):
    global ans
    if ans < dist:
        ans = dist
    visited[y][x] = 1 # 방문처리

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0<= ny < N and 0<= nx < N) and not visited[ny][nx]:
            if _map[ny][nx] < _map[y][x]:
                # visited[ny][nx] = 1 재귀 돌면서 어차피 방문처리가 되므로 해줄 필요가 없음.
                dfs(ny, nx, dist+1, K)
                #백트래킹
                visited[ny][nx] = 0
                

            elif K and K > _map[ny][nx] - _map[y][x]: #그 다음 봉우리가 더 높은 경우 
                tmp = _map[ny][nx]
                _map[ny][nx] = _map[y][x] - 1
                dfs(ny,nx,dist+1,0)
                visited[ny][nx] = 0
                _map[ny][nx] = tmp

                # for cut in range(1,K+1): 
                #     if _map[ny][nx] - cut < _map[y][x]:
                #         visited[ny][nx] = 1
                #         dfs(ny, nx, dist + 1, 0)
                #         #백트래킹
                #         visited[ny][nx] = 0
                #         dfs(ny, nx, dist, K)

T = int(input())
for tc in range(1,T+1):
    #n: 한 변의 길이. k: 최대 공사 가능 깊이
    N,K = map(int, input().split())
    _map = [list(map(int, input().split())) for _ in range(N)]
    
    # 최대 높이 찾기
    top = 0
    for i in range(N):
        top = max(top, max(_map[i]))

    
    ans = 1
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            #최대 높이와 같을 경우 dfs
            if _map[i][j] == top:
                dfs(i,j,0,K)
                visited[i][j] = 0

    print("#{num} {res}".format(num=tc, res = ans))

