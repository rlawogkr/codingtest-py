import sys

def input():
    return sys.stdin.readline().rstrip()


n = int(input())
arr = [0]*(n+1) #0 1 1 2 ...

arr[0] = 0
arr[1] = 1
for i in range(2, n+1):
    arr[i] = arr[i-2] + arr[i-1]
print(arr[n])