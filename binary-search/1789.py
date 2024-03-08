# 서로 다른 자연수 N개의 자연수의 합이 S. 자연수 N의 최댓값?
import sys


def input():
    return sys.stdin.readline().rstrip()

def total_sum(val):
    return val * (val + 1) // 2

def binarysearch(start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if total_sum(mid) > S:
            end = mid - 1
        elif total_sum(mid) < S:
            start = mid + 1
        else:
            return mid
    return end

S = int(input())
print(binarysearch(1, S))
# 1 2 3 4 5 ... 200
