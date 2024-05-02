import sys

def input():
    return sys.stdin.readline().rstrip()

#N: 유저 수, M: 관계 수
N, M = map(int, input().split())
INF = 1e9

# 인접 행렬 초기화
adj_array = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    adj_array[i][i] = 0
for _ in range(M):
    st, en = map(int, input().split())
    adj_array[st][en] = 1
    adj_array[en][st] = 1

#floyd-warshall
for k in range(1, N+1): # 거쳐가는 경로
    for i in range(1, N+1):
        for j in range(1, N+1):
            adj_array[i][j] = min(adj_array[i][j], adj_array[i][k] + adj_array[k][j])

res_arr = [sum(adj_array[i][1:]) for i in range(1, N+1)]
min_val = min(res_arr)
for i in res_arr:
    if min_val == i:
        print(res_arr.index(i)+1)
        break

'''
[[1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0], 
[1000000000.0, 0, 2, 1, 1, 2], 
[1000000000.0, 2, 0, 1, 2, 3], 
[1000000000.0, 1, 1, 0, 1, 2], 
[1000000000.0, 1, 2, 1, 0, 1], 
[1000000000.0, 2, 3, 2, 1, 0]]
'''

