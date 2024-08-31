# 서로 다른 옷의 조합 수 return
def solution(clothes):
    answer = 0
    dict_cloth = dict()

    for cloth, category in clothes:
        if category not in dict_cloth.keys():
            dict_cloth[category] = []
            dict_cloth[category].append(cloth)
        else:
            dict_cloth[category].append(cloth)

    cnt = []

    for i in dict_cloth.values():
        cnt.append(len(i)+1)
    ans = cnt[0]
    for i in range(1,len(cnt)):
        ans *= cnt[i]
    ans -= 1

    return ans