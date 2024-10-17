# [가장 먼저 탈락하는 사람의 번호, 자신의 몇 번째 차례에 탈락하는지]
# n: 참가하는 사람. 1부터 시작
from collections import defaultdict

def solution(n, words):
    answer = []
    people = defaultdict(list) # 1 ~ n 까지의 key값. 기본값을 list로 설정
    people[1].append(words[0])
    for i in range(1, len(words)):
        person_num = (i%n) + 1

        # string값의 끝글자와 그다음 string의 앞글자가 다르거나, words[i]가 이미 포함된 경우 종료
        if words[i-1][-1] != words[i][0] or (words[i] in words[:i]):
            return [person_num, len(people[person_num]) + 1]
        people[person_num].append(words[i])

    if words[len(words)-2][-1] != words[len(words)-1][0] or (words[-1] in words[:-1]):
        person_num = (len(words)-1)%n + 1
        return [person_num, len(people[person_num]) + 1]

    return [0,0]


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))