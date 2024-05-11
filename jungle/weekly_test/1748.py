import sys
# 1748. 수 이어 쓰기 1
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
answer = 0
length = 1

while N >= 10**length:
    answer += (10**length - 10**(length-1)) * length
    length += 1

answer += (N - 10**(length-1) + 1) * length
print(answer)