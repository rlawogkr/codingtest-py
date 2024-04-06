import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split()) #물품의 수, 최대 무게
lst = [[0,0]]#w,v
for _ in range(N):
    lst.append(list(map(int, input().split())))
dp = [[0]*(K+1) for _ in range(N+1)]
#dp[i][j]: i번째 무게를 넣었을 때, j까지 채워진 무게의 가치.
for i in range(1, N+1): # 1번물품부터 N번물품까지
    for j in range(1, K+1):
        w = lst[i][0]
        v = lst[i][1]

        if j < w: #w가 j를 넘으면 
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])