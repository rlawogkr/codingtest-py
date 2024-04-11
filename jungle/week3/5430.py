# import sys

# def input():
#     return sys.stdin.readline().rstrip()
    
# T = int(input())  # testcase 수

# for _ in range(T):
#     p = input()  # 수행할 함수. RDD
#     n = int(input())  # 배열에 들어있는 수의 개수
#     arr = input()[1:-1].split(',')  # 첫 번째와 마지막 괄호 제거 후 쉼표로 split
#     res = []
#     for num in arr:
#         if num.isdigit():  # 숫자인 경우에만 추가
#             res.append(int(num))

#     reverse_flag = False  # Reverse 여부 기록

#     error_flag = False  # Error 여부 기록

#     for cmd in p:
#         if cmd == 'R':
#             reverse_flag = not reverse_flag  # Reverse 연산일 경우 Flag 변경
#         elif cmd == 'D':
#             if not res:  # 배열이 비어있는 경우 Error 출력 후 종료
#                 error_flag = True
#                 break
#             if reverse_flag:  # Reverse 상태에 따라 삭제 위치 변경
#                 res.pop()
#             else:
#                 res.pop(0)

#     if error_flag:  # Error Flag가 True인 경우
#         print('error')
#     else:
#         if reverse_flag:  # Reverse 상태에 따라 결과 출력 방식 변경
#             print('[{}]'.format(','.join(map(str, res[::-1]))))
#         else:
#             print('[{}]'.format(','.join(map(str, res))))

import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input()) #testcase 수


for _ in range(T):
    p = input()  # 수행할 함수. RDD
    n = int(input())  # 배열에 들어있는 수의 개수
    arr = input()[1:-1].split(',')  # 첫 번째와 마지막 괄호 제거 후 쉼표로 split
    res = []
    
    for num in arr:
        if num.isdigit():  # 숫자인 경우에만 추가
            res.append(int(num))
    rank = []
    for i, num in enumerate(arr):
        rank.append((i,num))    
    
    if not res:
        print('error')
        continue
    
    for i in p:
        if i == 'R':
            rank.sort(key = lambda x: x[0], reverse=True)
        elif i == 'D':
            if rank:
                rank.pop(0)
            else:
                print('error')
                break
    if rank:
        print(rank)
    