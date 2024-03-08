import sys


def input():
    return sys.stdin.readline().rstrip()

def hanoi(n, start, end, via):
    global count
    if n == 1: 
        res.append(str(start)+" "+str(end))
        count += 1
    else:
        hanoi(n-1, start, via, end) #n-1개의 원판을 start에서 via로 옮김.
        res.append(str(start)+" "+str(end)) #가장 위 원판을 start에서 end로 옮김.(한개 남은 아래 원판)
        count += 1
        hanoi(n-1, via, end, start)# n-1개의 원판을 via에서 end로 옮김.



res = []
n = int(input())  # 장대에 쌓인 원판 개수
count = 0

dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)] # [i,st,en] i: 원판의 갯수. st: 시작. en: 목적지 
hanoi(n,1,3,2)
print(count)
print("\n".join(res))


