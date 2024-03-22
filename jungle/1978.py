import sys

input = sys.stdin.readline

n = int(input().rstrip())
_list = map(int, input().split())

#1과 자기자신으로만 나눠지는 수
def find_prime(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0: cnt += 1
    if cnt == 2: return True
    else: return False

_cnt = 0
for i in _list:
    if find_prime(i): _cnt += 1

print(_cnt)


