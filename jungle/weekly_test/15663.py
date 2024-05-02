import sys
#15663. N과 M (9)
def input():
    return sys.stdin.readline().rstrip()

# 사전 순으로 증가, 중복 없이 M개를 고른 수열
N, M = map(int, input().split()) # 4 2
arr = list(map(int, input().split())) # 1 7 9 9
arr.sort()
visited = [False] * N
res = []
def backtracking(arr, n):
    if n == M:
        print(' '.join(map(str, res)))
        return

    tmp = 0
    for i in range(0, N):
        if not visited[i] and arr[i] != tmp:
            res.append(arr[i])
            visited[i] = True
            tmp = arr[i] # 마지막에 들어온 값으로 초기화

            backtracking(arr, n+1)
            res.pop(-1)
            visited[i] = False

backtracking(arr, 0)