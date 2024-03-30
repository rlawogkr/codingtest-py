import sys

input = sys.stdin.readline

arr = [int(input().rstrip()) for i in range(9)]

for i,k in enumerate(arr):
    if k == max(arr):
        print(k)
        print(i+1)
