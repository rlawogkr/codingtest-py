# 하나 하나 만들 때마다 dic에 값을 추가
_map = {}
def make_dic(phone):
    global _map
    if str not in _map:
        _map[phone] = 1
    else:
        _map[phone] += 1



def solution(phone_book):

    for phone in phone_book:
        make_dic(phone)
        for key in _map:
            if key != phone and key.startswith(phone):
                return False
    return True

print(solution(["123", "3123"]))