import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())

def multi(a,b,c):
    if b == 1:
        return a%c
    tmp = multi(a,b//2,c)
    
    if b%2 == 0: #b가 짝수일 경우
        return tmp * tmp % c
    else: #b가 홀수일 경우
        return tmp * tmp * a % c

print(multi(a,b,c))
          