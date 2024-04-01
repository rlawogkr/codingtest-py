import sys

#음수를 양수로 나눌 때?: 양수로 바꾼 뒤 몱을 취하고, 그 몫을 음수로 바꿈.
#만들 수 있는 식의 결과의 최대, 최소를 구하기.
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -sys.maxsize
min_val = sys.maxsize

def dfs(i, sum):
    global max_val, min_val, add, sub, mul, div
    if i == len(data):
        max_val = max(max_val, sum)
        min_val = min(min_val, sum)
        return
    if add > 0:
        add -= 1
        dfs(i+1, sum+data[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i+1, sum-data[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i+1, sum*data[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i+1, int(sum/data[i]))
        div += 1
dfs(1, data[0])
print(max_val)
print(min_val)


# print(arr)
# print(operation)