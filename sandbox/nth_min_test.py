import heapq

def nth_smallest(n, arr):
    heap = arr[:] # 배열 복사
    heapq.heapify(heap) #배열을 힙으로 만듦.
    # for i in arr:
    #     heapq.heappush(heap, i)

    nth_min = None
    for _ in range(n):
        nth_min = heapq.heappop(heap)

    return nth_min

print(nth_smallest(2, [4,1,7,3,8,5]))