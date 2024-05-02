'''
숫자로만 이루어진 문자열 s
멋쟁이 숫자?
1. 길이가 3인 s의 substring을 10진수로 읽은 숫자
2. 각 자리의 숫자가 모두 같음

멋쟁이 숫자가 여러 개 존재하는 경우 가장 큰 수를 반환
멋쟁이 숫자가 존재하지 않을 경우 -1 반환

s = "12223"
return 222

s = "111999333"
return 999

s = "10009"
return 0
'''
s = "10029"
def solution(s):
    answer = -1
    n = len(s)
    for i in range(n-2):
        if s[i] == s[i+1] == s[i+2]:
            answer = max(answer, int(s[i:i+3]))

    return answer

print(solution(s))