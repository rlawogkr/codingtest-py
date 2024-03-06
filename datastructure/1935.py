# import sys
# from collections import deque

# input = sys.stdin.readline  # input을 sys.stdin.readline으로 바꿔줌.

# N = int(input())
# arr = input().strip()
# oper = "+-*/"
# dic = {}
# stack = []
# num = deque() # 숫자를 담을 deque

# for _ in range(N):
#     num.append(int(input()))

# # 숫자를 dic에 넣어줌. 값을 할당. {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
# for i in arr:
#     if i not in dic and i not in oper:
#         dic[i] = num.popleft() 

# print(dic)

# for i in arr:
#     if i not in oper:
#         stack.append(dic[i]) # 연산자가 아닐 경우, stack에 숫자를 넣어줌.
#     else:
#         if i == "+":
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(b + a)
#         elif i == "-":
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(b - a)
#         elif i == "*":
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(b * a)
#         else:
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(b / a)

# print(f"{stack[0]:.2f}")


import sys
n = int(sys.stdin.readline())
expression = sys.stdin.readline().rstrip()
values = []
stack = []

for _ in range(n):
    operand = int(sys.stdin.readline())
    values.append(operand)

for exp in expression:
    if exp.isalpha():
        stack.append(values[ord(exp)-65]) # ord('A') = 65
    else:
        rightNum = stack.pop()
        leftNum = stack.pop()

        if exp == '*':
            stack.append(leftNum * rightNum)
        elif exp == '+':
            stack.append(leftNum + rightNum)
        elif exp == '-':
            stack.append(leftNum - rightNum)
        elif exp == '/':
            stack.append(leftNum / rightNum)

print(f'{stack[0]:.2f}')
