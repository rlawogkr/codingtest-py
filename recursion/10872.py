import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

if n == 0: print(1)
else:
    fact_list = [i for i in range(1,n+1)]
    res = 1
    for i in fact_list:
        res *= i
    print(res)