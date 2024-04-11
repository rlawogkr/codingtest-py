import sys


def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()  # 2 4 5
s = []
def check(s):
    flag = True
    for i in range(1,len(s)):
        if s[i-1] > s[i]:
            flag = False
            break
    return flag


def backtracking(idx):
    if len(s) == m and check(s):
        print(" ".join(map(str, s)))
        return
    for i in range(idx, n):
        if s.count(arr[i]) == 0:
            s.append(arr[i])
            backtracking(idx + 1)
            s.pop()  # 미방문 처리


backtracking(0)
