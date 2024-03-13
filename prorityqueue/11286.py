import sys
import heapq # 리스트를 minHeap처럼 다룰 수 있도록 해줌.


def input():
    return sys.stdin.readline().rstrip()


n = int(input())  # 연산의 갯수
heap = []
res = []
# x != 0 : 배열에 x라는 값을 넣음.
# x == 0 : 배열에서 절대값 가장 작은 값 출력, 그 값을 배열에서 제거.

for _ in range(n):
    x = int(input())
    if x == 0:
        if not heap:
            res.append(0)
        else:
            tmp = heapq.heappop(heap) 
            res.append(tmp[1])
    else:
        heapq.heappush(heap, (abs(x), x))
# print("=========answer==========")
# print(res)
print("\n".join(map(str,res)))
