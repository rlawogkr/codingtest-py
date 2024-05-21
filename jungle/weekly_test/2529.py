import sys

#2529. 부등호
def input():
    return sys.stdin.readline().rstrip()

#최댓값, 최솟값 출력
#[0,1,2,3, ... 9]
n = int(input())
sign = input().split() # ['<', '>', '<', '>', '<', '>', '<', '>', '<']
check = [False] * 10 # 0 ~ 9
max_val = ""
min_val = ""

def checker(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def dfs(cnt, s):
    global max_val, min_val
    if cnt == n + 1:
        if not min_val:
            min_val = s
        else: # 마지막이 최대
            max_val = s
        return
    for i in range(10):
        if not check[i]:
            # 첫 번째 숫자인 경우 or 부등호를 만족하는 경우
            # s[-1]: 왼쪽값 str(i): 들어오는 값 sign[cnt - 1]: 부등호
            if cnt == 0 or checker(s[-1], str(i), sign[cnt - 1]):
                check[i] = True
                dfs(cnt + 1, s + str(i))
                check[i] = False

dfs(0, "")
print(max_val)
print(min_val)