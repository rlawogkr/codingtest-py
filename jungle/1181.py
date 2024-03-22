import sys

input = sys.stdin.readline

n = int(input())

arr = list(set([input().rstrip() for _ in range(n)]))

_arr = sorted(arr, key = lambda x: (len(x),x))
print("\n".join(_arr))