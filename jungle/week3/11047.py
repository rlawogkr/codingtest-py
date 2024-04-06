import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
#K원을 만드는데 필요한 동전 개수 최소값
cnt = 0
# print(coins) # [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
for coin in coins:
    if K < coin:
        continue
    while True:
        if K < coin:
            break
        else:
            cnt += 1
            K -= coin


print(cnt)