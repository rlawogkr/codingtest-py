tc = int(input())

def check(arr):
    count = 0 # 몇 개를 구매했는지?
    val = 0 # 현재 가격
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]: # 증가하는 순열. 구매할 것.
            val -= arr[i-1]
            count += 1
        else: # 같거나 감소하는 순열. 팔 것.  + count * arr[i]
            val += (arr[i-1])*count
            count = 0
    if arr[len(arr)-2] < arr[len(arr)-1]:
        val += (arr[len(arr)-1])*count
    return val

for i in range(1, tc+1):
    n = int(input()) # 개수
    arr = list(map(int, input().split()))
    print("#{} {}".format(i, check(arr)))
