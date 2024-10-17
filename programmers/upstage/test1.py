def solution(line):
    answer = ""
    n = len(line)
    i = 0

    while i<n:
        if line[i].isupper(): # 대문자일 경우
            answer += line[i]
            i += 1

            # 대문자가 연속되면 계속 진행
            while i<n and line[i].isupper():
                if i+1 < n and line[i+1].islower():
                    break
                i += 1

            # 소문자가 있으면 해당 단어 끝까지 이동
            while i<n and line[i].islower():
                i += 1
        else:
            i += 1
    return answer

print(solution("OneHundredPeopleFromUSAAndMexico"))
