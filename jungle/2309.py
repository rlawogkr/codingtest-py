import sys
from itertools import combinations

input = sys.stdin.readline

_list = [int(input().rstrip()) for _ in range(9)]

_sum = sum(_list)
for i in combinations(_list, 2):
    if _sum - (i[0] + i[1]) == 100:
        _list.remove(i[0])
        _list.remove(i[1])
        break

_list.sort()
print("\n".join(map(str,_list)))
    