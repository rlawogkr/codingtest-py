import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

testcase = int(input())

for _ in range(testcase):
    n, m = map(int, input().split()) # n: 문서의 갯수 m: 궁금한 문서 인덱스
    arr = list(map(int, input().split())) # 각 문서의 중요도 1 2 3 4

    dq = deque()
    #중요도쌍 초기화
    for i in range(len(arr)):
        dq.append((i, arr[i])) # idx, 중요도. 튜플로 이루어진 덱.
    
    cnt = 0
    # 이렇게 하면 튜플을 리턴 (0,5) (3,4) (2,9) 이런 식으로
    # 여기서 x는 각 deque의 요소. 즉 (i, arr[i])와 같은 튜플.
    print(max(dq, key = lambda x: x[1]))
    while dq:
        if dq[0][1] == max(dq, key = lambda x: x[1])[1]: #맨앞값의 중요도가 가장 클 경우
            cnt += 1
            if dq[0][0] == m:
                print(cnt)
                break
            else:
                dq.popleft()
        else:
            dq.append(dq.popleft())
            

    