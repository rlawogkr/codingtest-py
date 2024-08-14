#1486. 등산

import sys
from heapq import heappush, heappop

def input():
    return sys.stdin.readline().rstrip()

# n: row, m: column, t: 높이의 차이, d: 어두워지는 시간
n, m, t, d = map(int, input().split())

tmp = [list(input()) for _ in range(n)]
mountain = [[] for _ in range(n)]

for i in range(n):
    for j in range(m):
        mountain[i].append(ord(tmp[i][j]) - 65)

# def dijkstra(st):


