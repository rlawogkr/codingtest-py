def count_different_by_one_digit(num1, num2):
    diff_count = 0
    while num1 > 0 and num2 > 0:
        if num1 % 10 != num2 % 10:  # 각 자리 숫자를 비교
            diff_count += 1
        num1 //= 10  # 한 자리씩 오른쪽으로 이동
        num2 //= 10
    return diff_count == 1 or diff_count == 0  # 딱 한 자리만 다른 경우 True

def solution(arr1, arr2):
    answer = []

    for num2 in arr2:
        count = 0
        for num1 in arr1:
            if count_different_by_one_digit(num1, num2):
                count += 1
        answer.append(count)

    return answer


arr1 = [123457, 123458, 123436, 123456, 223344, 113344]
arr2 = [123456, 123344, 223455]

print(solution(arr1, arr2))  # [4, 2, 0]
