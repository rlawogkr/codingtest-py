import sys
from heapq import heappush, heappop
def input():
    return sys.stdin.readline().rstrip()

# 아이를 만날 때마다 자신이 들고 있는 가장 가치 선물 하나를 선물해줌
# 아이들과 거점지의 정보가 주어짐
# 아이들에게 준 선물들의 가치 출력

n = int(input())
gift = list()

for _ in range(n):
    arr = list(map(int, input().split())) # arr[0] 개의 선물을 충전
    if arr[0] == 0:
        if not gift:
            print(-1)
        else:
            print(-heappop(gift))
    else:
        for j in range(arr[0]):
            heappush(gift, -arr[j+1])