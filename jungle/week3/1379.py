# 1379 강의실2
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

heap = []
N = int(input())
arr = []
room = [0]*(N) # 강의실 번호

for _ in range(N):
    idx, st, en = map(int, input().split())
    arr.append((st, en, idx-1))

arr.sort() 
res = 0
for st, en, idx in arr:
    if heap and heap[0][0] <= st: # 가장 빨리 끝나는 강의실을 찾아서 배정
        room[idx] = room[heap[0][2]]
        heapq.heappop(heap)
    else:
        res += 1
        room[idx] = res
    heapq.heappush(heap, (en, st, idx))

print(res)
for r in room[1:]:
    print(r)
# print(room)