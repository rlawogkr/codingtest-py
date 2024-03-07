import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


testcase = int(input())
    

for _ in range(testcase):
    size, edge = map(int, input().split()) # 정점의개수(size), 간선의개수

    for _ in range(edge): # 간선에 대한 정보. 2회 반복
        u, v = map(int, input().split()) # 각 줄에 인접한 두 정점의 번호



