import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

#각 칸이 검은색. 흰색으로만 칠해져 있음.
graph = [input().split() for _ in range(M)]

print(graph)