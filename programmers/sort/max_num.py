import functools
numbers = [60,1,2]
#4자리수까지 비교 가능.
def comparator(a,b):
    if a+b > b+a: return 1
    else: return -1

def solution(numbers):
    str_num = list(map(str, numbers))
    tmp = sorted(str_num, key = functools.cmp_to_key(comparator))
    answer = ""
    return "".join(tmp)

print(solution(numbers))