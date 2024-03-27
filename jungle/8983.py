import sys
input = sys.stdin.readline

#M: 사대의 수, N: 동물의 수, L: 사정거리
M,N,L = map(int, input().split())
guns = list(map(int, input().split()))
guns.sort()

#사로의 시작점st, 사로의 끝점en, 동물이있을때맞출수있는사정거리L x좌표, 동물이있을때맞출수있는사정거리R y좌표
def binary_search(st, en, l_target, r_target):
    while st <= en:
        mid = (st + en) // 2
        tmp = guns[mid]
        #사로가 해당 동물의 왼쪽끝 위치, 오른쪽끝 위치 사이에 있으면
        if l_target <= tmp <= r_target:
            return True
        if tmp > l_target:
            st = mid + 1
        if tmp < r_target:
            en = mid - 1
    return False

res = 0
for _ in range(N):
    x, y = map(int,input().split()) #동물 위치
    
    if y > L: continue
    else:
        r_target = x + L - y # 동물을 맞출 수 있는 오른쪽끝 x좌표
        l_target = x - (L - y) # 동물을 맞출 수 있는 왼쪽끝 x좌표
        if binary_search(0, M-1, l_target, r_target):
            res += 1
print(res)