# 2579 계단오르기
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input()) # 계단의 개수
arr = [0]*(n+1) # 계단의 점수
dp = [0]*(n+1) # 계단의 최대 점수
for i in range(1, n+1):
    arr[i] = int(input())
dp[1] = arr[1]

if n > 1:
    dp[2] = arr[1] + arr[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

print(dp[n])
