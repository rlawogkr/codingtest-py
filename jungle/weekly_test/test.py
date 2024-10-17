from collections import deque

def ferris_wheel_time(n, times):
    # 관람차의 칸을 deque로 초기화
    ride_queue = deque()

    # 초기 관람차의 칸에 처음 n명 타는 사람 넣기
    for i in range(n):
        if i < len(times):
            ride_queue.append(times[i])
        else:
            ride_queue.append(0)  # 사람이 더 없으면 0으로 채움

    time_elapsed = 0  # 총 시간
    waiting_times = deque(times[n:])  # 아직 타지 않은 사람들

    while ride_queue:
        # 1초가 지남 -> 모든 deque의 시간이 1초씩 줄어든다
        for i in range(len(ride_queue)):
            if ride_queue[i] > 0:
                ride_queue[i] -= 1

        # 맨 앞에서 내리고 맨 뒤에서 새로 탄다
        if waiting_times:
            # 앞에서 내림
            ride_queue.popleft()
            # 뒤에 사람이 타고 있을 경우 새로 탑승
            ride_queue.append(waiting_times.popleft())
        else:
            # 대기 인원이 없으면 0 추가
            ride_queue.popleft()
            ride_queue.append(0)

        # 1초 흐름
        time_elapsed += 1

        # 모든 사람이 타고 내렸다면 종료
        if all(time == 0 for time in ride_queue):
            break

    return time_elapsed

# 예시 사용
n = 2
times = [4, 5, 1]
result = ferris_wheel_time(n, times)
print(result)  # 총 소요 시간 출력
