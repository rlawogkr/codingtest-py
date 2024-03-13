import sys

def custom_key(obj):
    return (obj[1], obj[0])

input = sys.stdin.readline

n = int(input())
arr = [[[] for _ in range(2)] for _ in range(n)]
for i in range(n):
    arr[i][0], arr[i][1] = map(int, input().split())

res = sorted(arr, key = lambda x:custom_key(x))

_list = []
for i in res:
    _list.append(str(i[0])+" "+str(i[1]))

print("\n".join(_list))

