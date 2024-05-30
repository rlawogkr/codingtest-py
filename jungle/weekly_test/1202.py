import sys
from heapq import heappop, heappush
def input():
    return sys.stdin.readline().rstrip()

# n: 보석의 개수, k: 가방의 개수
# 각 가방에 담을 수 있는 최대 무게 Ci
# 가방에는 최대 1개의 보석만 넣을 수 있다.
n, k = map(int, input().split())
jewels = []
for _ in range(n):
    jewels.append(list(map(int, input().split()))) # 보석의 무게, 보석의 가치
bags = []
for _ in range(k):
    bags.append(int(input())) # 가방의 무게

# [[5, 23], [2, 99], [1, 65]]
jewels.sort(key= lambda x: -x[0]) # 보석의 무게가 무거운 순으로 정렬
# [2, 10]
bags.sort() # 가방의 무게가 작은 순으로 정렬

result = 0
heap = []
for bag in bags:
    while jewels and bag >= jewels[-1][0]: # 가방에 넣을 수 있는 보석들을 모두 heap에 넣기
        heappush(heap, -jewels.pop()[1]) # 가치가 높은 순으로 넣기
    if heap:
        result -= heappop(heap)

print(result)

# 가장 좁은 공간에 가장 높은 가치를 넣을 것
# result = 0
# for bag in bags:
#     for jewel in jewels:
#         if jewel[0] <= bag:
#             result += jewel[1]
#             jewels.remove(jewel)
#             break
#
# print(result)
