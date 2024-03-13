import heapq

visited = [False] * 3
print(visited)

_visited = [False for _ in range(3)]
print(_visited)
s = [[] for i in range(3)]

heap = []
heapq.heappush(heap,50)
heapq.heappush(heap,10)
heapq.heappush(heap,30)
heapq.heappush(heap,70)
heapq.heappush(heap,90)
heapq.heappush(heap,20)

res = []

while heap:
    res.append(int(heapq.heappop(heap)))

print(" ".join(map(str,res)))
print(*res)

# _tuple = (1,2)
# _tuple[0] = 2

dict = {1:2, 2:4}
print(dict)
dict[1] = 3
print(dict)

print(ord("-"))