import sys

input = sys.stdin.readline

_score = int(input())

for i in range(1,10):
    print(str(_score)+' * '+ str(i)+' = '+str(_score*i))