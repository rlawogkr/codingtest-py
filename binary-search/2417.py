import sys

def input():
    return sys.stdin.readline().rstrip()


def binarysearch(start, end):
    global answer

    while start <= end:
        mid = (start + end) // 2
        if mid ** 2 >= N:
            answer = mid
            end = mid - 1
        else: start = mid + 1

N = int(input())
answer = 0
binarysearch(0, N)
print(answer)

