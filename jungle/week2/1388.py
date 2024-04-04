# 기훈이의 방바닥 장식하는데 필요한 나무판자의 개수
import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
floor = [list(input()) for _ in range(N)]
#print(floor)
answer = 0
for i in range(N):
    for j in range(M):
        if floor[i][j] == '-':
            if j == 0 or floor[i][j - 1] != '-': 
                answer += 1
        else:
            if i == 0 or floor[i - 1][j] != '|':
                answer += 1
print(answer)