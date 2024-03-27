import sys
input = sys.stdin.readline
n,b = map(int, input().rstrip().split()) #행렬의 크기 n(2<=n<=5), b(1<=b<=100~00)
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

def multi(a,b):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    return result

# n이 홀수일 경우, n이 짝수일 경우
def solve(a,b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a
    
    tmp = solve(a,b//2)
    if b % 2 != 0: #홀수인 경우
        return multi(multi(tmp,tmp), a)
    else: #짝수인 경우
        return multi(tmp,tmp)

result = solve(arr,b)

for i in range(n):
    print(*result[i])
