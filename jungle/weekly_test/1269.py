import sys
# 1269. 대칭 차집합
def input():
    return sys.stdin.readline().rstrip()

a,b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

print(len(A-B) + len(B-A))


