import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
result = []

for _ in range(n):
    x = int(input())

    if not x: 
        if not heap: result.append(0)
        else:result.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)

print("\n".join(map(str, result)))