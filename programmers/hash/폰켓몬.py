# 포켓몬 n//2 마리는 가져갈 수 있음
# 같은 종류는 같은번호
# 최대한 다양한 종류의 포켓몬을 가지길 원함
def solution(nums):
    answer = 0
    _map = {}
    for num in nums:
        if num not in _map:
            _map[num] = 1
        else:
            _map[num] += 1

    if len(_map) >= len(nums)//2: # n//2보다 종류가 많은 경우
        answer = len(nums)//2
    else:
        answer = len(_map)

    return answer

print(solution([3,1,2,3])) # 2