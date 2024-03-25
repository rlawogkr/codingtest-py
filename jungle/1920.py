import sys

input = sys.stdin.readline

# st는 0, en은 len(_arr) - 1. 인덱스로 접근. val은 _num의 인자
def binary_search(st, en, val):
    global _arr
    global _num
    while st <= en:
        mid = (st + en) // 2
        if _arr[mid] == val: return 1
        elif _arr[mid] > val: en = mid - 1
        else: st = mid + 1
    return 0
    

n = int(input().rstrip())
_arr = [int(i) for i in input().rstrip().split()] #비교 대상
_arr.sort()

m = int(input().rstrip())
_num = [int(i) for i in input().rstrip().split()]

for i in range(len(_num)):
    print(binary_search(0, len(_arr)-1, _num[i]))