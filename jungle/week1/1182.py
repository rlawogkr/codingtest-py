import sys
input = sys.stdin.readline
n,s = map(int, input().split()) #n개의 정수로 이루어진 수열, 합이 s
arr = list(map(int, input().split()))

cnt = 0
def dfs(idx, sum):
    global cnt
    if idx == n:return
    if sum + arr[idx] == s: cnt += 1
    dfs(idx+1, sum) # 현재 인덱스를 더하지 않는 경우
    dfs(idx+1, sum + arr[idx]) # 현재 인덱스를 더하는 경우

dfs(0,0)
print(cnt)