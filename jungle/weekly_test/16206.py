import sys
from heapq import heappush, heappop
def input():
    return sys.stdin.readline().rstrip()
# 길이가 10인 롤케이크를 최대한 많이 만드려고 함
# return: 길이가 10인 롤케이크 개수의 최대값
n, m = map(int, input().split()) # n: 롤케이크의 개수 m: 자를 수 있는 최대 개수
cakes = list(map(int, input().split()))

cakes.sort()
q = []
for i in range(1, n):
    heappush(q, cakes[i] - cakes[i-1])

ans = cakes[-1] - cakes[0] + 1
for _ in range(min(m-1, n-1)):
    ans -= heappop(q)

print(ans)