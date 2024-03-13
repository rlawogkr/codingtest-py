##시간 초과

import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

#그냥 정렬안된 리스트 넘어옴, 해당 리스트의 마지막 인덱스, idx = len(list) - 1
def find_middle(arr, idx):
    mid = idx // 2
    sorted_list = []
    heap = arr[:] # 값 복사
    heapq.heapify(heap)
    while heap:
        sorted_list.append(heapq.heappop(heap))
    return sorted_list[mid]
    

result = [] #답을 넣을 리스트.
arr = [] #정렬 안된 리스트.


n = int(input()) # 1 <= n && n <=100000
for i in range(n):
    val = int(input())
    arr.append(val)
    result.append(find_middle(arr, i))

print("\n".join(map(str, result)))