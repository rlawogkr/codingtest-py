_map = [[1,2,3,4],[5,6,7,8],[8,4,65,5],[5,6,7,8]]

top = 0
for i in range(4):
    top = max(top, max(_map[i]))

# print(top)

arr = [1,2,3]
def functionScope(lst):
    lst[0] = 999
    print(lst)

functionScope(arr)
print(arr)


