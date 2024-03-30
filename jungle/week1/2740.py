import sys
input = sys.stdin.readline

n,m = map(int, input().split())#크기 n*m
A = [list(map(int,input().split())) for _ in range(n)]

m,k = map(int, input().split())#크기 m,k
B = [list(map(int,input().split())) for _ in range(m)]

answer = [[0]*k for _ in range(n)]

for _n in range(n):
    for _k in range(k):
        for _m in range(m):
            answer[_n][_k] += A[_n][_m] * B[_m][_k]

# 결과 출력
for row in answer:
    print(*row)


