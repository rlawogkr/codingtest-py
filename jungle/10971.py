import sys

input = sys.stdin.readline

n = int(input().rstrip())

_list = [[0]*n for i in range(n)]

for i in range(n):
    for j,val in enumerate(map(int, input().rstrip().split())):
        _list[i][j] = val

print(_list)
    