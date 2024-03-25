#순서대로 K번째 사람을 제거.
#한 사람이 제거되면 남은 사람들로 원을 따라 이 과정을 계속한다.
#N명의 사람이 모두 제거될 때까지 계속된다.
import sys
from collections import deque

input = sys.stdin.readline
dq = deque()
n, k = map(int, input().rstrip().split())

for i in range(1, n+1):
    dq.append(i)

res = []
while dq:
    for _ in range(k-1):
        dq.rotate(-1)
    res.append(dq.popleft())

_str = ", ".join(map(str, res))
print('<'+_str+'>')