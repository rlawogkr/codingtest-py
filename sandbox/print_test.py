
arr = [[[] for _ in range(2)] for _ in range(3)]
_arr = [[]*2 for _ in range(3)]

__arr = [0]*5

for _item in _arr:
    print(id(_item))

zero_list = [0]*3
print(zero_list[0])
zero_list[0] = 2

for i in zero_list:
    print(id(i))



