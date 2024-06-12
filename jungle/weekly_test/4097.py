# 4097. 수익
import sys
def input():
    return sys.stdin.readline().rstrip()

while True:
    n = int(input())
    if n == 0:
        sys.exit()

    dp = [0] * n  # dp[i]: i일까지의 최대 수익
    dp[0] = int(input())
    for i in range(1,n):
        val = int(input())
        dp[i] = max(dp[i-1] + val, val)

    print(max(dp))
