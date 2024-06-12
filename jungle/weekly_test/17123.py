# 17123. 배열 놀이
import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n,M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    res = [[] for _ in range(2)]

    # row 값의 합
    for i in range(n):
        res[0].append(sum(matrix[i]))
    # col 값의 합
    for i in range(n):
        res[1].append(sum(matrix[m][i] for m in range(n)))

    for _ in range(M):
        r1,c1,r2,c2,v = map(int,input().split())
        # c1~c2행까지 (r2-r1)*v만큼 증가.
        for i in range(r1-1,r2):
            res[0][i] += (c2 - c1 + 1) * v
        # r1~r2열까지 (c2-c1)*v만큼 증가.
        for i in range(c1-1,c2):
            res[1][i] += (r2 - r1 + 1) * v

    for i in range(2):
        print(*res[i])