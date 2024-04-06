import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input()) # 테스트 케이스
for _ in range(T):
    N = int(input()) # 지원자의 숫자
    employee = [tuple(map(int, input().split())) for _ in range(N)] #각각의 순위
    employee.sort(key = lambda x:x[0]) # 서류순위, 면접순위
    # [(1, 4), (2, 5), (3, 6), (4, 2), (5, 7), (6, 1), (7, 3)]
    print(employee)
    cnt = 1
    tmp = 0
    for i in range(1, N):
        if employee[i][1] < employee[tmp][1]: # 면접순위가 높을 경우
            tmp = i
            cnt += 1

    print(cnt)
