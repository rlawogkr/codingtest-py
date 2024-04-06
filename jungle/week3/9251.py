import sys

def input():
    return sys.stdin.readline().rstrip()

str1 = input() #n
str2 = input() #m

n = len(str1)
m = len(str2)

_map = [[0]*(n+1) for _ in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if str1[j-1] == str2[i-1]: # 같을 경우 
            _map[i][j] = _map[i-1][j-1] + 1
        else:
            _map[i][j] = max(_map[i-1][j], _map[i][j-1])

print(_map[m][n])
