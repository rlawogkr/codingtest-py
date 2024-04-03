# 구슬 찾기. N은 홀수, 무게가 전체의 중간인 구슬을 찾기.
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

adj_list_1 = [[] for _ in range(n+1)]
adj_list_2 = [[] for _ in range(n+1)]


for _ in range(m):
    a,b = map(int, input().split()) # a가 b보다 무겁다.
    adj_list_1[a].append(b)
    adj_list_2[b].append(a)

# 2단계: DFS 함수 생성
def dfs(adj, v1, parent, results):
    if v1 in adj:
        for v2 in adj[v1]:
            if v2 not in parent:
                parent[v2] = v1
                dfs(adj, v2, parent, results)
    results.append(v1)

# 3단계: 각 정점을 시작점으로 DFS를 실행했을 때, 해당 정점의 자손 개수를 카운트
answers = set()
for v1 in range(1, n+1):
    # 정방향 그래프 탐색 (오름차순)
    parent, results = {}, []
    parent[v1] = None
    dfs(adj_list_1, v1, parent, results)
    # 본인을 제외한 자손들의 수 확인
    # - 본인 제외 자손들의 수가 (N+1)//2 이상이면 본인은 가운데에 올 수 없음
    # - 가령, 구슬이 5개일 때, 자손이 3개 이상이면 본인의 인덱스는 중간인 2보다 커짐
    if len(results)-1 >= (n+1)//2:
        answers.add(v1)
        continue
    # 역방향 그래프 탐색 (내림차순)
    parent, results = {}, []
    parent[v1] = None
    dfs(adj_list_2, v1, parent, results)
    if len(results)-1 >= (n+1)//2:
        answers.add(v1)

print(len(answers))