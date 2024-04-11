import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
arr = list(map(int, input().split()))
# print(arr) [10, 20, 10, 30, 20, 50]
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            

print(max(dp))