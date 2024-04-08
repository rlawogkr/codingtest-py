import sys

def input():
    return sys.stdin.readline().rstrip()

M = int(input())

_set = set()
for _ in range(M):
    command = input().split()
    if len(command) == 2:
        cmd = command[0]
        val = int(command[1])
    else:
        cmd = command[0] 

    if cmd == 'add':
        _set.add(val)
    elif cmd == 'remove':
        if not _set:
            continue
        _set.remove(val)
    elif cmd == 'check':
        if val in _set:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if val in _set:
            _set.remove(val)
        else:
            _set.add(val)
    elif cmd == 'all':
        _set.update(range(1,21))
    else:
        _set.clear()