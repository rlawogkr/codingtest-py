_list = [4,2,1,3,1]

sorted_list = sorted(_list)
print(_list, sorted_list)

wanna_eat = [
    ('chicken', 17900, 'Puradak'),
    ('Pizza', 21000, 'Domino'),
    ('Spagetti', 12000, 'Mola')
]

order_by_asc_price = sorted(wanna_eat, key = lambda x: x[1])
order_by_desc_price = sorted(wanna_eat, key = lambda x: x[1], reverse= True)
print(order_by_asc_price, order_by_desc_price)

_list1 = [21,61, 4, 31, 65, 98,21]
_list2 = [66,12,34,58,91,3,21]
_dict = dict(zip(_list1, _list2))
sorted_dict = sorted(_dict) #이렇게 할 경우, key값만 정렬된다.
sorted_dict = sorted(_dict.items()) #이렇게 할 경우, key값만 정렬된다.
print(sorted_dict)