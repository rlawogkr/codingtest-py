import sys
from collections import deque
# 1로 만들기
def input():
    return sys.stdin.readline().rstrip()

def cal(val, i):
    if i ==0 and val%3 ==0:
        return val//3
    elif i ==1 and val%2 ==0:
        return val//2
    else:
        return val-1

visited = [False] * 1000001
numbers = [0]*1000001
def bfs(x):
    q= deque()
    q.append(x)
    visited[x] = True
    while q:
        a = q.popleft()
        for i in range(3):
          nx = cal(a,i)
          if nx < 0 or nx > a:continue
          if visited[nx] or numbers[nx] != 0: continue
          q.append(nx)
          visited[nx] = True
          numbers[nx] = numbers[a] + 1

n = int(input())
numbers[n] = 1
bfs(n)
print(numbers[1]-1)
