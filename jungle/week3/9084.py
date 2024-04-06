import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input()) #테스트의 개수
res = []
for _ in range(T):
    N = int(input()) #동전의 가지 수
    coins = list(map(int,input().split()))
    
    M = int(input()) #만들어야 하는 금액
    
    #초기화
    dp = [0]*(M+1) 
    dp[0] = 1
    

    for coin in coins:
        for j in range(coin, M+1):
            dp[j] += dp[j - coin]   
    res.append(dp[M])

print("\n".join(map(str,res)))
