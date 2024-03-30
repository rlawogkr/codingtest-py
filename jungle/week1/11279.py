import sys
import heapq

input = sys.stdin.readline
n = int(input().rstrip())
heap = []

res = []
for _ in range(n):
    x = int(input().rstrip())

    if x == 0:
        if not heap:res.append(0)
        else:res.append(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)

print("\n".join(map(str,res)))

