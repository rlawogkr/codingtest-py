import sys

# 적당히 어려운 문제를 골라냄.
# 적당히 어려운 문제? 상위 25% 이내의 난이도를 가진 문제 중 가장 쉬운 문제.
# 각 문제의 난이도는 정해져 있음, 정수로 표기
'''
1 <= N <= 10000
1 <= levels[i] <= 2147483647
levels[i]는 서로 다름

answer : 조건에 맞는 문제의 난이도를 반환. 25% 이내의 난이도를 가진 문제 중 가장 쉬운 문제
조건에 해당하는 문제가 없을 경우 -1 반환

'''
levels= [1,2,3,4]
# 25% 이내의 난이도를 가진 문제 중 가장 쉬운 문제
def solution(levels):
    answer = 0
    # 9,8,7,6,5,4,3,2,1
    levels.sort(reverse=True)
    idx = int(len(levels)*0.25) #
    answer = levels[idx-1]
    return answer

print(solution(levels))