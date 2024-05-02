#9935 문자열 폭발
import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(string, bomb):
    stack = []
    for s in string:
        stack.append(s)
        if len(stack) >= len(bomb):
            if stack[-len(bomb):] == list(bomb):
                for _ in range(len(bomb)):
                    stack.pop()
    return ''.join(stack) if stack else 'FRULA'

string = input()
bomb = input() # 폭발 문자열
print(solution(string, bomb))