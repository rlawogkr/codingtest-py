import sys
import heapq

max_heap = []
arr = [1,2,3,4,5]
for i in arr:
    heapq.heappush(max_heap, (-i, i))
    


order, max_val = heapq.heappop(max_heap)  # 튜플
print(order, max_val)
