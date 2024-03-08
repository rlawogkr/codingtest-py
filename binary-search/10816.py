import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()

n = int(input()) # 숫자 카드 개수
n_list = list(map(int, input().split())) # 숫자 카드에 적힌 정수들
# n_list.sort() # [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
counter = Counter(n_list) # Counter({10: 3, -10: 2, 3: 2, 2: 1, 6: 1, 7: 1}

print(type(counter))
m = int(input())
m_list = list(map(int, input().split())) # 숫자카드가 몇개인지에 대한 변수
for i in m_list:
    if i in counter:
        print(counter[i], end = " ")
    else:
        print(0, end = " ")