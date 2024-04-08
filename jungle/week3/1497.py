import sys
from itertools import combinations

# 1497. 기타콘서트
def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split()) #N: 기타의 개수, M: 곡의 개수

arr = [input().split() for _ in range(N)]

# ['GIBSON', [1, 0, 1, 1, 0]], 
# ['FENDER', [0, 0, 0, 1, 1]], 
# ['TAYLOR', [1, 1, 1, 1, 1]]
for guitar_score in arr:
    tmp = []
    for i in guitar_score[1]:
        if i == 'Y':
            tmp.append(1)
        else:
            tmp.append(0)
    guitar_score[1] = tmp


# ['GIBSON', [1, 0, 1, 1, 0]],
# ['FENDER', [0, 0, 0, 1, 1]],
# ['TAYLOR', [1, 1, 1, 1, 1]]
answer = 0
for comb in combinations(arr, M):
    score = [0] * 5
    for guitar_score in comb:
        for i in range(5):
            score[i] += guitar_score[1][i]
    answer = max(answer, sum([i**2 for i in score]))







