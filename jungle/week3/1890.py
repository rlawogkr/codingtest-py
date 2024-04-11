# 1890 점프
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)] # 게임판. 오른쪽, 아래로만 이동 가능
dp = [[0]*n for _ in range(n)] # dp[i][j]: (i, j)까지 도달할 수 있는 경로의 수

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if dp[i][j] == 0:
            continue
        if i+arr[i][j] < n:
            dp[i+arr[i][j]][j] += dp[i][j]
        if j+arr[i][j] < n:
            dp[i][j+arr[i][j]] += dp[i][j]

print(dp[n-1][n-1])
