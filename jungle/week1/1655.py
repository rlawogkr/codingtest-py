import sys
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

min_heap = [] #최소힙
max_heap = [] #최대힙
res = []
for i in range(n):
    
    if len(min_heap) == len(max_heap):# key, value
        heapq.heappush(max_heap, (-arr[i], arr[i]))
    else:
        heapq.heappush(min_heap, (arr[i], arr[i]))

    if min_heap and max_heap and min_heap[0][1] < max_heap[0][1]:
        (tmpA, valA) = heapq.heappop(min_heap)
        (tmpB, valB) = heapq.heappop(max_heap)
        
        heapq.heappush(min_heap, (-tmpB, valB))
        heapq.heappush(max_heap, (-tmpA, valA))
    
    res.append(max_heap[0][1])

print("\n".join(map(str,res)))