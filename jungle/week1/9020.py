import sys

input = sys.stdin.readline

test_case = int(input().rstrip())


def find_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

#n보다 작은 소수 p들을 찾음. 처음 n - p < p 일 때 탈출
#n 출력, n-p출력
for _ in range(test_case):
    arr = []
    n = int(input().rstrip())
    for i in range(2,n+1):
        if find_prime(i):arr.append(i)
    
    a=0
    b=0
    
    for p in arr:
        if n-p in arr:
            if p >= n-p: 
                a = n-p
                b = p
                break
    print(a, b)
