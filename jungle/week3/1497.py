import sys

def search(idx, guitar_mask, g_count):
    global min_guitar_count, max_count

    # 현재 연주 가능한 곡의 개수
    bit_count = bin(guitar_mask).count("1")

    # 현재 최대값은 같지만, 사용한 기타의 수가 더 작을 때
    if bit_count == max_count and g_count < min_guitar_count:
        min_guitar_count = g_count

    # 현재 최대값보다 더 많은 곡을 칠 수 있을 때
    if bit_count > max_count:
        min_guitar_count = g_count
        max_count = bit_count

    # 모든 곡을 칠 때, 모든 기타를 확인했을 때
    if bit_count == M or idx == N:
        return

    # 현재 기타를 사용할 때
    search(idx + 1, guitar_mask | guitar_bit[idx], g_count + 1)
    # 현재 기타를 사용하지 않을 때
    search(idx + 1, guitar_mask, g_count)


# 입력값 처리
N, M = map(int, input().split())
guitar_bit = [0] * N

for i in range(N):
    input_values = input().split() # 값: [기타의 개수, 기타의 여부]
    input_values.pop(0)  # 기타의 개수 제거
    guitar_tf = input_values[0]
    # 'Y' = 1, 'N' = 0 비트 형태로 변경
    for j in range(M):
        if guitar_tf[j] == 'Y':
            guitar_bit[i] |= (1 << j)

min_guitar_count = sys.maxsize
max_count = 0

# 백트래킹을 통해서 탐색 진행
search(0, 0, 0)

# 연주할 수 있는 곡이 없을 때
if min_guitar_count == 0:
    min_guitar_count = -1

# 기타의 개수 출력
print(min_guitar_count)
