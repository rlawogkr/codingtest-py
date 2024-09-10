# s가 1이 될 때까지 계속해서 s에 이진 변환을 가함
# [이진 변환의 횟수, 제거된 모든 0의 개수]
def change_to_bin(val): # 정수값을 2진수로 변환
    res = []
    while val//2:
        res.append(str(val%2))
        val = val//2
    res.append(str(val%2))
    res.reverse()
    return ''.join(res)


def solution(s):
    ans = []

    cnt_a = 0 # 이진 변환 횟수
    cnt_b = 0 # 제거된 0의 수

    while True:
        for chr in s:
            if chr == '0':
                cnt_b += 1
            else:
                ans.append(1)
        s = change_to_bin(len(ans))
        if s == '1':
            break

    return [cnt_a, cnt_b]

print(solution("110010101001")) # [3, 8]