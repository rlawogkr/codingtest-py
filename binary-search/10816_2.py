import sys

def input():
    return sys.stdin.readline().rstrip()

def lower_bound(n_list, target):
    start = 0
    end = len(n_list)
    mid = (start + end) // 2

    while start < end:
        if n_list[mid] >= target:
            end = mid
        else:
            start = mid + 1
        mid = (start + end) // 2
    return start

def upper_bound(n_list, target):
    start = 0
    end = len(n_list)
    mid = (start + end) // 2
    while start < end:
        if n_list[mid] > target:
            end = mid
        else:
            start = mid + 1
        mid = (start + end) // 2
    return start

n = int(input()) # 숫자 카드 개수
n_list = list(map(int, input().split())) 
n_list.sort() # [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]

m = int(input()) # 찾아야하는 숫자 개수
m_list = list(map(int, input().split())) # [10, 9, -5, 2, 3, 4, 5, -10]

res = []
for i in m_list:
    lower = lower_bound(n_list, i)
    upper = upper_bound(n_list, i)
    res.append(upper - lower)

print(' '.join(map(str, res))) # 3 0 0 1 2 0 0 2