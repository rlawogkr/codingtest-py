import sys
#6064. 카잉달력
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
# M: 1~40000, N: 1~40000. <M: N>이 카잉 달력의 마지막 해
# x: 1~M, y: 1~N. <x: y>가 현재 해. 유효하지 않은 표현일 경우 -1 return.

for _ in range(T):
    M, N, x, y = map(int, input().split()) # k번째 해
    while x <= M*N:
        if x % N == y % N:
            print(x)
            break
        x += M # x에 M을 더해주면서 다음 해로 넘어감.
    else:# x가 M*N보다 커지면 유효하지 않은 표현
        print(-1)