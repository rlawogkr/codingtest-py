array = [i for i in range(3)] # [0,1,2]
sorted(array, reverse=True)

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1씩 감소하며 반복. 0번째 인덱스는 제외
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else: break

print(array)