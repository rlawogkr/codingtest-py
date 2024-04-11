import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(set(map(int,input().split())))
arr.sort() # 1 7 9 9

# print(arr)
res = []
def dfs(idx):
    if len(res) == M:
        print(" ".join(map(str,res)))
        return
    
    for i in range(idx, len(arr)):
        res.append(arr[i])    
        dfs(i)
        res.pop()

dfs(0)