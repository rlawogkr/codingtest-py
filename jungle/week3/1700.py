import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split()) #멀티탭 구현 
arr = list(map(int, input().split()))

power_bar = []
cnt = 0

for i in range(K):
    if arr[i] in power_bar:
        continue
    elif len(power_bar) < N:
        power_bar.append(arr[i])
    else:
        max_idx = -1
        max_power = -1
        for j in range(N):
            try:
                # 가장 나중에 사용될 전기 용품의 인덱스를 찾음
                idx = arr[i:].index(power_bar[j])
                if idx > max_idx:
                    max_idx = idx
                    max_power = j
            # 가장 나중에 사용될 전기 용품이 없을 경우
            except ValueError: 
                max_power = j
                break
        # 가장 나중에 사용될 전기 용품을 제거하고 새로운 전기 용품 연결
        power_bar[max_power] = arr[i]
        cnt += 1

print(cnt)
