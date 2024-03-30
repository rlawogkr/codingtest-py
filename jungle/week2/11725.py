#트리의 루트: 1
#각 노드의 부모를 구하는 프로그램
#각 노드의 부모 번호를 2번 노드부터 순서대로 출력
import sys
from collections import deque
input = sys.stdin.readline

node_len = int(input().rstrip()) #노드 개수 7개

#adj_list 초기화
# [[], [4, 6], [4], [5, 6], [1, 2, 7], [3], [1, 3], [4]]
adj_list = [[] for _ in range(node_len + 1)]
for _ in range(node_len-1):
    v1, v2 = map(int, input().rstrip().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)
for i in range(1, node_len + 1):
    adj_list[i].sort()

v = [False] * (node_len +1)
parent_node = [0] * (node_len +1)
def bfs(idx):
    dq = deque()
    dq.append(idx)
    v[idx] = True

    while dq:
        for i in adj_list[idx]:
            if not v[i]:
                v[i] = True
                parent_node[i] = idx
                dq.append(i)
                break
        dq.popleft()

bfs(1)
for i in range(2, node_len+1):
    print(parent_node[i])