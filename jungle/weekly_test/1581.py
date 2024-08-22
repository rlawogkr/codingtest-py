import sys

def input():
    return sys.stdin.readline().rstrip()


arr = list(map(int, input().split())) # [FF: 0, FS: 1, SF: 2, SS: 3]
ans = 0

# 빠른 곡으로 시작하는 것이 없는 경우
if arr[0] == 0 and arr[1] == 0 and arr[2] != 0 and arr[3] != 0:
    ans = arr[3] + 1  # SF, SS가 존재할 경우 SS 전부 담고 마짐박 SF 1개 추가
elif arr[0] == 0 and arr[1] == 0 and arr[2] == 0 and arr[3] != 0:
    ans = arr[3]  # SS만 존재할 경우 SS 전부 담기
elif arr[0] == 0 and arr[1] == 0 and arr[2] != 0 and arr[3] == 0:
    ans = 1  # SF만 있을 경우 1개 추가

# 빠른 곡으로 시작하는 것이 있는 경우
else:
    if arr[0] != 0 and arr[1] == 0: # FS 곡이 없는 경우
        ans += arr[0]  # FF 개수만큼 추가
    elif arr[0] != 0 and arr[1] != 0:  # FF와 FS가 모두 존재할 때
        ans += arr[0] + 1  # FF 전부 추가하고 마지막에 FS 추가
        arr[1] -= 1
        ans += arr[3]  # SS 전부 추가

        if arr[1] >= arr[2]:
            ans += arr[2] * 2  # SF 시퀀스를 모두 사용
        else:
            ans += arr[1] * 2 + 1  # FS를 모두 사용하고 SF를 하나 더 추가

    elif arr[0] == 0 and arr[1] != 0:  # FF가 없을 경우
        ans = 1  # FS로 시작
        arr[1] -= 1
        ans += arr[3]  # SS 시퀀스를 모두 추가

        if arr[1] >= arr[2]:
            ans += arr[2] * 2  # SF 시퀀스를 모두 사용
        else:
            ans += arr[1] * 2 + 1  # FS를 모두 사용하고 SF를 하나 더 추가

print(ans)

