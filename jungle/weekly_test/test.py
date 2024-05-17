list_arr = [9,2,3,4]

def sort_list(lis):
    res = []
    for i in range(len(lis)-1, -1, -1):
        res.append(lis[i])
    return res

print(sort_list(list_arr))
