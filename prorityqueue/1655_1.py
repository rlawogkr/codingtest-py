import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


n = int(input())

max_heap = []  # 내림차순
min_heap = []  # 오름차순
result = []

for _ in range(n):
    val = int(input())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-val, val))
    else:
        heapq.heappush(min_heap, (val, val))

    if len(max_heap) > 0 and len(min_heap) > 0 and max_heap[0][1] > min_heap[0][1]:
        (max_order, max_val) = heapq.heappop(max_heap)  # 튜플
        (min_order, min_val) = heapq.heappop(min_heap)  # 튜플
        heapq.heappush(min_heap, (-max_order, max_val))
        heapq.heappush(max_heap, (-min_order, min_val))
    result.append(max_heap[0][1])

print("\n".join(map(str, result)))

# 3 2 1 8 9
