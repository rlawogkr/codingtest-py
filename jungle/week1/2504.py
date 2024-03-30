# () : 괄호열의 값은 2
# [] : 괄호열의 값은 3
# 입력이 올바르지 못한 괄호열이면 반드시 0을 출력.
import sys
input = sys.stdin.readline

stack = []
_list = [int(i) if i.isdigit() else i for i in input().rstrip()]


answer = 0
tmp = 1
for i in range(len(_list)):

    if _list[i] == "(":
        stack.append(_list[i])
        tmp *= 2

    elif _list[i] == "[":
        stack.append(_list[i])
        tmp *= 3

    elif _list[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if _list[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else: # "]"
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if _list[i-1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack: print(0)
else: print(answer)
            
    

