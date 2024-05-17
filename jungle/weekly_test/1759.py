import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

l,c = map(int, input().split()) # 서로 다른 l개의 소문자 선택, 주어지는 문자 수
arr = list(map(str, input().split()))
arr.sort()

lis = list(combinations(arr, l))

res = []
for obj in lis:
    consonant = 0 #자음
    vowel = 0 #모음
    tmp = ""
    for i in obj:
        if i in "aeiou":
            vowel += 1
            tmp += i
        else:
            consonant += 1
            tmp += i
    if consonant >=2 and vowel >=1:
        res.append(tmp)

print("\n".join(res))



