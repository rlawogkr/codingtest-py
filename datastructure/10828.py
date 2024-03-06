import sys

def input():
    return sys.stdin.readline().strip()

n = int(input()) # 명령의 수

stack = []

# 모든 입력 받기
commands = [input().split() for _ in range(n)]

# 입력 처리
for cmd in commands:
    val = 0
    if len(cmd) == 2:
        val = int(cmd[1])
    cmd = cmd[0]
    
    if cmd == 'push':
        stack.append(val)
    elif cmd == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) == 0: 
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(stack) == 0: 
            print(-1)
        else: 
            print(stack[-1])
