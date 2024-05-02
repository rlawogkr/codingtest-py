import sys

def input():
    return sys.stdin.readline().rstrip()

def backtracking(list, n, start):
    if n == 6:
        for i in range(len(list)):
            if visited[i]:
                print(list[i], end=' ')
        print()
        return

    for i in range(start, len(list)):
        if not visited[i]:
            visited[i] = True
            backtracking(list, n+1, i+1)
            visited[i] = False

while True:
    lis = list(map(int,input().split()))
    if lis[0] == 0:
        break
    visited = [False] * len(lis)
    backtracking(lis[1:], 0, 0)
    print()
