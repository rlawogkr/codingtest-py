import sys

def input():
    return sys.stdin.readline().rstrip()

# 0~N 까지의 정수 K개를 더함, 그 합이 N이 되는 경우의 수
N, K = map(int, input().split())

#dp[k][n] : k개를 더해, n을 만듦
dp = [[0]*(N+1) for _ in range(K+1)]

for i in range(N+1):
    dp[1][i] = 1

print(dp)
for i in range(2, K+1):
    for j in range(N+1):
        for l in range(j, -1, -1):
            dp[i][j] += dp[i-1][j-l]
            dp[i][j] %= 1000000000


print(dp[K][N])