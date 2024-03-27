import sys
import heapq

# 입력값 받기
n = int(sys.stdin.readline().strip())
locations = [] # ([(시작 좌표, 끝 좌표) ...]
for _ in range(n):
    h, o = map(int, sys.stdin.readline().strip().split())
    # 집과 사무실 중 좌표값이 낮은 것을 앞에, 좌표값이 높은 것을 뒤에 넣어줌
    locations.append((min(h, o), max(h, o)))
d = int(sys.stdin.readline().strip())

# 선분의 끝점을 기준으로 오름차순 정렬한 다음, 앞점을 기준으로 오름차순 정렬
locations.sort(key=lambda x: (x[1], x[0]))

heap = []
max_cnt = 0