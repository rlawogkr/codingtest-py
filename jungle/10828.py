import sys
input = sys.stdin.readline

n = int(input().rstrip())

stack = []
for _ in range(n):
    command = input().rstrip().split()
    if len(command) == 2:
        command[1] = int(command[1])
    
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if not stack: print(-1)
        else: print(stack.pop())
    elif command[0] == 'size': print(len(stack))
    elif command[0] == 'empty':
        if not stack: print(1)
        else: print(0)
    elif command[0] == 'top':
        if not stack: print(-1)
        else: print(stack[len(stack)-1])