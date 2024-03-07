import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

val = list(map(int, input().split())) # 종이에 적힌 수

#덱 초기화
dq = deque()
for i in range(n):
    dq.append((i, val[i]))

_list = []
# print(dq)
# deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])

while dq:
    _tuple = dq[0]

    if _tuple[1] > 0:
        dq.popleft()
        _list.append(str(_tuple[0]+1))
        dq.rotate(-(_tuple[1]-1)) # 왼쪽으로 회전
    
    else:
        dq.popleft()
        _list.append(str(_tuple[0]+1))
        dq.rotate(abs(_tuple[1]))


print(" ".join(_list))
