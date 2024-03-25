#각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지
import sys
input = sys.stdin.readline

n = int(input().rstrip())
towers = [int(i) for i in input().rstrip().split()]

stack = [] # 최대값을 저장
res = []

for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:  # 수신 가능한 상황
            res.append(stack[-1][0] + 1)
            break
        else: # 마지막 값이 수신 가능하지 않음.
            stack.pop()
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        res.append(0)
    stack.append((i, towers[i]))  # 인덱스, 값

print(" ".join(map(str, res)))


