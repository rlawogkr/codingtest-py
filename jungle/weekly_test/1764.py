import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

a = set() # 듣도 못한 사람. N. 둘째 줄~N개의 줄
b = set() # 보도 못한 사람. M
res = []

for i in range(N+M-1):
    if i <= N-1:
        a.add(input())
    else:
        b.add(input())

for i in a:
    if i in b:
        res.append(i)
res.sort()
res_str = [len(res)]

for i in res:
    res_str.append(i)


print("\n".join(map(str, res_str)))
