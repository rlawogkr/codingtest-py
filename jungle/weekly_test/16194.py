#16194. 카드 구매하기 2
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input()) #민규가 구매하려고 하는 카드 개수

#카드1개, 카드2개, ... 카드N개 -> N가지
#카드 i개를 구매하는데 드는 비용은 P[i]원.
P = [0] + list(map(int, input().split()))

#dp[i] : 카드 i개를 구매하는데 드는 최소 금액
dp = [0] + [1e9] * N

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + P[j])

print(dp[N])
