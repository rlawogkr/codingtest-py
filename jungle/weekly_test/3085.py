import sys
# 3085. 사탕 게임
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
board = [list(input()) for _ in range(N)]

def check(board):
    max_count = 1
    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]: # 가로로 연속된 사탕의 개수
                count += 1
            else:# 연속된 사탕이 끊기면
                count = 1
            max_count = max(max_count, count)

        count = 1
        for j in range(1, N):
            if board[j][i] == board[j-1][i]: # 세로로 연속된 사탕의 개수
                count += 1
            else: # 연속된 사탕이 끊기면
                count = 1
            max_count = max(max_count, count)

    return max_count

max_count = 0
for i in range(N):
    for j in range(N):
        if j+1 < N: # 가로로 연속된 사탕의 위치를 바꿈.
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            max_count = max(max_count, check(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i+1 < N: # 세로로 연속된 사탕의 위치를 바꿈.
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            max_count = max(max_count, check(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(max_count)