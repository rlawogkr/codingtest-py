import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
#[[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
arr = [list(map(int, input().split())) for _ in range(n)]
max_size = -int(1e9)
def dfs(idx, total):
    global max_size
    if idx >= n:
        max_size = max(max_size, total)
        return
    if idx + arr[idx][0] <= n:
        dfs(idx + arr[idx][0], total + arr[idx][1])
    dfs(idx + 1, total)

dfs(0, 0)
print(max_size)