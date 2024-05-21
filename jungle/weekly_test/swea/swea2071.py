tc = int(input())

for i in range(1, tc+1):
    arr = list(map(int, input().split()))
    print("#{} {}".format(i,round(sum(arr)/10),1))