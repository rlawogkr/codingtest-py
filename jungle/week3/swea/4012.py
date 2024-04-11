import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input()) # testcase
def dfs(st, ingredients, visited):
    if len(visited) == ingredients:

for _ in range(T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    # 재료의 갯수
    ingredients = N//2
    
    # 1 2 3, 1 3 2, 2 1 3, 2 3 1, 3 1 2, 3 2 1
