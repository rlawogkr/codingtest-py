# 문자열이 입력으로 주어지면 학습을 시킴
# 학습된 단어들을 순서대로 찾을 때, 몇 개의 문자를 입력하면 되는지?



def make_list(words):
    arr = []

    for idx in range(len(words)):
        word = words[idx]
        tmp = ""
        new_list = [words[j] for j in range(len(words)) if j!=idx] # ['go', 'guild']

        for w in word:
            tmp += w
            for i in range(len(new_list)):
                if tmp in new_list[i]:
                    break
                else:
                    arr.append()



    return arr


def solution(words):
    answer = 0
    words.sort()

    print(make_list(words))

    return answer

words = ["go","gone","guild"]
print(solution(words))