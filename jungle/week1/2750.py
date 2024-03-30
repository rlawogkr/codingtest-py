import sys

input = sys.stdin.readline

n = int(input().rstrip())


_list = []
for _ in range(n):
    _list.append(int(input().rstrip()))

_list.sort()
print("\n".join(map(str,_list)))