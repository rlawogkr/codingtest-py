# 1부터 n까지 번호가 붙어있음.
# 1번카드가 제일 위, n번카드가 제일 아래.

# 제일 위에 있는 카드를 바닥에 버림.(1을 버림)
# 그 다음 제일 위에 있는 카드(2)를 제일 아래 있는 카드 밑으로 옮김. 2를 마지막으로 옮김.

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dq = deque()

n = int(input())

for i in range(1,n+1):
    dq.append(i)

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())
#1 2 3 4 5 6
#2 3 4 5 6

