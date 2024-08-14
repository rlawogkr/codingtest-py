import sys

# 2482. 색상환
def input():
    return sys.stdin.readline().rstrip()

# n: 색상환의 색상 개수, k: 선택할 색상의 개수
n = int(input())
k = int(input())

dp = [[0] * (n+1) for _ in range(4)] # dp[i][j]: i번째 색상까지 사용하여 j개의 색상을 선택하는 경우의 수

# 1번째 색상을 선택하는 경우의 수
for i in range(1,4):
    dp[i][1] = n-i

for i in range(2,4):
    for j in range(2,n+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000003

print(sum(dp[3][k:])) # 3번째 색상까지 사용하여 k개의 색상을 선택하는 경우의 수의 합 (k ~ n