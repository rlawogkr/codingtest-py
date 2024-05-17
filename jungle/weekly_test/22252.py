# import sys
#
# # 입력을 빠르게 받기 위해 sys.stdin.readline() 사용
# def input():
#     return sys.stdin.readline().rstrip()
#
# q = int(input())  # 쿼리의 개수
#
# # Key: 고릴라의 이름, Value: 정보의 가치를 저장하는 딕셔너리
# map_dict = {}
#
# total = 0
#
# for _ in range(q):
#     # 한 줄을 읽고 공백으로 나눈 값을 리스트로 저장
#     line = input().split()
#
#     # 쿼리의 타입, 고릴라 이름, 정보의 개수를 각각 변수에 저장
#     type = line[0]
#     name = line[1]
#     num = int(line[2])
#
#     # 처음 등장한 고릴라라면
#     if name not in map_dict:
#         map_dict[name] = []
#
#     # 정보를 얻는 쿼리인 경우
#     if int(type) == 1:
#         # 보유하고 있는 정보의 개수만큼 반복하며 정보를 리스트에 추가
#         for i in range(3, len(line)):
#             map_dict[name].append(int(line[i]))
#         # 고릴라가 가지고 있는 정보 리스트를 내림차순으로 정렬
#         map_dict[name].sort(key=lambda x: -x)
#
#     # 정보를 구매하는 쿼리인 경우
#     elif int(type) == 2:
#         # 고릴라가 가지고 있는 정보 리스트가 비어있지 않고,
#         # 구매할 정보의 개수가 0보다 큰 경우에만 실행
#         while map_dict[name] and num > 0:
#             # 내림차순으로 정렬한 리스트의 첫 번째 요소를 더하고, 리스트에서 제거
#             total += map_dict[name].pop(0)
#             num -= 1
#
# # 총 정보 가치 출력
# print(total)

import sys
def input():
    return sys.stdin.readline().rstrip()

dic = {}
count = 0 #리턴할 값

tc = int(input())

for _ in range(tc):
    arr = input().split()

    if int(arr[0]) == 1: # 상인이 얻은 정보. dic에 값을 채움.
        if arr[1] not in dic:
            dic[arr[1]] = [] # dic 생성
            for i in range(3, len(arr)):
                dic[arr[1]].append(int(arr[i]))

        else: # 이미 값이 있을 경우
            for i in range(3, len(arr)):
                dic[arr[1]].append(int(arr[i]))

        dic[arr[1]].sort(reverse=True) #내림차순 정렬

    elif int(arr[0]) == 2: #호석이 사는 정보. count를 업데이트
        val = int(arr[2])
        if arr[1] in dic:
            while val>0 and dic[arr[1]]:
                count += dic[arr[1]].pop(0) #0번 인덱스의 값을 pop
                val -= 1


print(count)

