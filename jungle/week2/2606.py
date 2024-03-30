import sys
input = sys.stdin.readline

# 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수
c_node = int(input().rstrip())
c_edge = int(input().rstrip())

#adj_list 초기화
adj_list = [[] for _ in range(c_node + 1)]
for _ in range(c_edge):
    st, en = map(int, input().rstrip().split())
    adj_list[st].append(en)
    adj_list[en].append(st)

visited = [False] * (c_node + 1)
def dfs(idx):
    visited[idx] = True # 1번컴퓨터에서 시작
    for com in adj_list[idx]:
        if not visited[com]:
            visited[com] = True
            dfs(com)

dfs(1)

print(visited.count(True) - 1)