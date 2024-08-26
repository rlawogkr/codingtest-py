global_dic = [] # 여기에 모든 배열을 저장
arr_dic = ["A", "E", "I", "O", "U"]
def make_word(base, depth):
    global_dic.append(base)
    if depth == 5:
        return
    for i in range(5):
        make_word(base + arr_dic[i], depth + 1)
def solution(word):
    cnt = 1
    for i in range(5):
        make_word(arr_dic[i], 1)

    for s in global_dic:

        if s != word:
            cnt += 1
        else:
            return cnt
    return cnt

print(solution("AAAE"))