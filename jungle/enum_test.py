import sys

input = sys.stdin.readline

arr = [0 for i in range(9)]

for i in range(9):
    arr[i] = int(input().rstrip())

new_arr = list(enumerate(arr))


tmp = sorted(new_arr,key = lambda x :x[1],reverse=True)



print(tmp[0][1])
print(tmp[0][0]+1)