import sys

def input():
    return sys.stdin.readline().rstrip()

n, c = map(int, input().split()) #n: 집의 개수, c: 공유기의 개수

router = [0]*n
for i in range(n):
    router[i] = int(input())

router.sort()
st = 1
en = router[len(router) -1] - router[0]

# 거리에 대한 이진 탐색
# 공유기 설치 시 인접한 두 공유기 사이의 설치 간격을 이진 탐색
# 설치한 공유기 개수 wifiCount 를 셈.
# [1, 2, 4, 8, 9]

def binary_search(st, en):
    mid = (st + en)//2 #길이
    while st <= en:
        count = 1 # 첫번째 공유기는 무조건 설치
        cur = router[0]
        for i in range(1, n):
            if router[i] >= cur + mid:
                count += 1
                cur = router[i] # 현재 위치를 다음 위치로 변경
        if count >= c: # 길이를 늘림
            st = mid + 1
        else: # 길이를 줄임
            en = mid - 1

        mid = (st + en)//2
    return mid

print(binary_search(st, en))


# print(router)

