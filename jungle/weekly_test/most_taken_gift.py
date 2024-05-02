# friends = ["muzi", "ryan", "frodo", "neo"]
# gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

# friends = ["a","b","c"]
# gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
# 두 사람이 선물을 주고 받았으면, 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받음.
# 두 사람이 선물을 주고받은 기록 없거나, 주고받은 수가 같으면, 선물지수가 더 큰 사람이 더 작은 사람에게 선물을 하나 받음.
# 선물 지수도 같을 경우 선물을 주고받음.

def solution(friends, gifts):
    gifted = {} # gifted = {"friend 이름": {"선물 준 친구 이름": 이 친구에게 준 선물 개수}}
    gift_idx = {} # 선물 지수
    # 딕셔너리 초기화
    for friend in friends:
        gifted[friend] = {}
        gift_idx[friend] = 0

    for gift in gifts:
        t, f = gift.split(' ') # t: 선물을 준 사람, f: 받은 사람

        if f in gifted[t]:# 해당 딕셔너리 안에 받은 사람이 있을 경우
            gifted[t][f] += 1
        else:
            gifted[t][f] = 1
        # 선물 지수 반영
        gift_idx[t] += 1
        gift_idx[f] -= 1

    # 각자 받게 될 선물 개수
    will_get = [0 for _ in friends]
    for i in range(len(friends)):
        curr = friends[i] # 인덱스 i에 해당하는 친구
        for j in range(i+1, len(friends)):
            another = friends[j] # 인덱스 j에 해당하는 친구
            # curr가 another에게 준 선물 개수
            a = gifted[curr][another] if another in gifted[curr] else 0
            # another가 curr에게 준 선물 개수
            b = gifted[another][curr] if curr in gifted[another] else 0

            if a > b: # curr가 선물을 더 많이 줬다면
                will_get[i] += 1
            elif a < b: # another가 선물을 더 많이 줬다면
                will_get[j] += 1
            elif a == b: # 둘이 선물을 주고 받은 개수가 같다면 선물 지수 확인
                ai, bi = gift_idx[curr], gift_idx[another]
                if ai > bi:
                    will_get[i] += 1
                elif ai < bi:
                    will_get[j] += 1

    answer = max(will_get)
    return answer

print(solution(friends, gifts))