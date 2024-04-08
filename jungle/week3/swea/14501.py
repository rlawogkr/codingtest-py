import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

counsel = [list(map(int, input().split())) for _ in range(N)]
#[[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
_max = -sys.maxsize

def backtracking(idx, cost):
    global _max
    if idx >= N:
        _max = max(_max, cost)
        return
    
        #해당 지점에 상담을 했을 경우
    if idx + counsel[idx][0] <= N:
        backtracking(idx + counsel[idx][0], cost + counsel[idx][1])
        #해당 지점에 상담 안했을 경우
    backtracking(idx + 1, cost)


backtracking(0, 0)
print(_max)