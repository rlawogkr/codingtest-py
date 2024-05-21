#11723. 집합

import sys
def input():
    return sys.stdin.readline().rstrip()

m = int(input())
s = set()
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            s = set([i for i in range(1,21)])
        else: # empty
            s = set()
    else:
        cmd, num = cmd
        num = int(num)
        if cmd == 'add':
            s.add(num)
        elif cmd == 'remove':
            if num in s:
                s.remove(num)
        elif cmd == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)