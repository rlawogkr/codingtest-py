from itertools import permutations

global_list = [] # 출력할 결과값
list_num = []

def is_prime(num): # 소수인지 판별
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def solution(numbers):
    list_num = list(numbers) # ['0','1','1']

    # str을 숫자로 바꾸고 값을 global_list에 넣음. 개수가 1개부터 len(list_num) -1 개까지
    for i in range(1, len(list_num)+1):
        for j in list(permutations(list_num, i)):
            print(j)
            tmp = int(''.join(j))
            print(tmp)
            if tmp not in global_list and is_prime(tmp):
                global_list.append(tmp)

    return len(global_list)

print(solution("011"))