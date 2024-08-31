# 1~n까지 번호를 받음
# 정확하게 순위를 매길 수 있는 선수의 수 return
from collections import deque
def solution(n, results):
    answer = 0
    adj_list = [[] for _ in range(n+1)]
    reversed_adj_list = [[] for _ in range(n+1)]


    # [[], [2], [5], [2], [3, 2], []]
    for i in range(len(results)):
        adj_list[results[i][0]].append(results[i][1])
        reversed_adj_list[results[i][1]].append(results[i][0])

    arr_out = [0] * (n+1)
    arr_in = [0] * (n+1)
    # 해당 지점에서 나가는 것
    for j in range(1, n+1):
        dq = deque()
        visited = [0] * (n+1)
        dq.append(j)
        visited[j] = 1
        while dq:
            cur = dq.popleft()
            for k in adj_list[cur]:
                if visited[k] == 0:
                    visited[k] = 1
                    dq.append(k)
        arr_out[j] = sum(visited)

    for j in range(1, n+1):
        dq = deque()
        visited = [0] * (n+1)
        dq.append(j)
        visited[j] = 1
        while dq:
            cur = dq.popleft()
            for k in reversed_adj_list[cur]:
                if visited[k] == 0:
                    visited[k] = 1
                    dq.append(k)
        arr_in[j] = sum(visited)
    sum_arr = [arr_out[i] + arr_in[i]-1 for i in range(n+1)]
    answer = sum([1 for i in sum_arr if i == n])

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) # 2