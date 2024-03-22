import sys

input = sys.stdin.readline
test_case = int(input().rstrip())

res = ""
for _ in range(test_case):
    _num, _str = input().split()
    _num = int(_num)
    for s in _str:
        res += s*_num
    res += '\n'

print(res)