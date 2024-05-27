import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split()) #n: row m: col
paper = [list(map(int, input())) for _ in range(n)]

max_val = 0

# using bitmasking
for i in range(1 << (n*m)): # ...00, ...01, ...10, ...11, ...100 ....
    sum = 0
    # 가로로 자르는 경우
    for j in range(n):
        cur = 0 # 현재 숫자를 저장할 변수를 초기화
        for k in range(m):
            #j*m + k는 1차원 배열의 인덱스
            idx = j*m + k
            # i의 idx번째 비트가 0이면 가로로 자르는 것
            if (i & (1 << idx)) == 0:
                cur = cur * 10 + paper[j][k] # 가로로 자르는 경우, 현재 숫자에 10을 곱하고 새로운 숫자를 더함.
            else:
                sum += cur
                cur = 0
        sum += cur

    # 세로로 자르는 경우
    for j in range(m):
        cur = 0
        for k in range(n):
            idx = k*m + j
            # i의 idx번째 비트가 1이면 세로로 자르는 것
            if (i & (1 << idx)) != 0:
                cur = cur * 10 + paper[k][j]
            else:
                sum += cur
                cur = 0
        sum += cur

    max_val = max(max_val, sum)

print(max_val)