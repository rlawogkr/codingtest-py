import sys
#14567. 선수과목
def input():
    return sys.stdin.readline().rstrip()

# 1과목 ~ N과목까지 차례대로 최소 몇 학기에 이수할 수 있는지?
n, m = map(int, input().split())
for _ in range(m):
    # a과목이 b과목의 선수과목
    a, b = map(int, input().split())