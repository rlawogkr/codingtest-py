# 변경 가능한 객체인 리스트를 매개변수로 전달하는 경우
def update_list(some_list):
    some_list.append(4)

my_list = [1, 2, 3]
update_list(my_list)
print(my_list)  # 출력: [1, 2, 3, 4]

# 불변한 객체인 정수를 매개변수로 전달하는 경우
def update_int(some_int):
    some_int += 1

my_int = 5

update_int(my_int)
print(my_int)  # 출력: 5 (변화 없음)
