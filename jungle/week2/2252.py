import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) #학생들 번호: n, 키 비교 횟수: m
# 1~n으로 생성
adj_list = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
dq = deque() 
#adj_list 초기화, indegree 배열 초기화    
for _ in range(m):
    st, en =  map(int, input().rstrip().split())
    adj_list[st].append(en)
    indegree[en] += 1

result = [] 
# 초기값 세팅
for idx in range(1, n+1):  
    if indegree[idx] == 0: 
        dq.append(idx)

# 인접 리스트와 indegree를 기반으로 dq를 초기화
while dq:
    node = dq.popleft()
    result.append(node)
    
    for next_node in adj_list[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            dq.append(next_node)


print(*result) # 위상 정렬 결과 출력