import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
#[[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1) # dp[i]: i번째 날까지의 최대 이익
max_size = 0
for i in range(n):
    if i + arr[i][0] <= n:
        # i번째의 가격을 포함.
        dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[i] + arr[i][1]) # i번째 날까지의 최대 이익 + i번째 날의 이익
    #i번째의 가격을 포함시키지 않음.
    dp[i + 1] = max(dp[i + 1], dp[i]) # i번째 날까지의 최대 이익을 i + 1번째 날까지의 최대 이익으로 넘겨줌
print(dp[n])
