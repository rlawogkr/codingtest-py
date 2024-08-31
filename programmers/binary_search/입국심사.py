# 접근 방식
# 7 * 4 + 20 * 2
def solution(n, times):
    answer = 0
    new_times = sorted(times) # 오름차순으로 정렬

    left = 0
    right = new_times[-1] * n # 최대 시간
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(len(new_times)): # 각 심사대에서 처리할 수 있는 인원 수
            cnt += mid // new_times[i]
        if cnt >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer
print(solution(6, [7, 10])) # 28