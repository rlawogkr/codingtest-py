import sys

def input():
    return sys.stdin.readline().rstrip()

def star(i, j, num):
    if i // num % 3 == 1 and j // num % 3 == 1: print(" ")
    else:
        if num // 3 == 0: print("*")
        else: star(i,j,num//3)

num = int(input())
for i in range(num):
    for j in range(num):
        star(i,j,num)
    print("\n")