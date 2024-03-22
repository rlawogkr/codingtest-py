import sys

input = sys.stdin.readline

_score = int(input())

def sol(_score):
    if 90 <= _score and _score <=100: print('A')
    elif 80 <= _score and _score <= 89: print('B')
    elif 70 <= _score and _score <= 79: print('C')
    elif 60 <= _score and _score <= 69: print('D')
    else: print('F')

sol(_score)