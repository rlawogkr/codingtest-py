import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
res = ""

for _ in range(n):
    arr = input()
    cnt = 0
    
    for i in arr:
        cnt += 1 if i == '(' else -1
        if cnt < 0:
            res += "NO\n"
            break
    else:
        res += "YES\n" if cnt == 0 else "NO\n"

print(res)


