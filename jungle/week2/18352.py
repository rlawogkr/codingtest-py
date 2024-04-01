import sys
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()

#도시의 개수: N, 도로의 개수: M, 거리정보: K, 출발도시 번호: X
N, M, K, X = map(int, input().split())
adj_list = [[] for _ in range(N+1)]

#단방향 그래프
for _ in range(M):
    st, en = map(int, input().split())
    adj_list[st].append(en)

#시작 인덱스를 넣음
dest = [sys.maxsize] * (N+1)

def dfs(st, cnt, dest_idx):
    global vis
    #그 지점을 한 번이라도 방문한 적이 있으면 종료.
    if vis[st]: return 
    if st == dest_idx:
        dest[dest_idx] = min(dest[dest_idx], cnt)
        return

    for i in adj_list[st]:
        dfs(i, cnt + 1, dest_idx)

for i in range(1, N+1):
    vis = [False] * (N+1)    
    dfs(X, 0, i)

res = []
for idx, value in enumerate(dest):
    if value == K:
        res.append(idx)

if not res:
    print(-1)
else:
    print("\n".join(map(str, res)))