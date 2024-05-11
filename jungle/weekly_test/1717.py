import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline().rstrip()

# m: 입력으로 주어지는 연산의 개수
n, m = map(int, input().split())

parent = [i for i in range(n+1)]
def find(node):
    if parent[node] == node:
        return node
    # 경로 압축
    parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    p_a = find(a)
    p_b = find(b)

    if p_a <= p_b:
        parent[p_b] = p_a #parent[b] = p_a : 이런 식으로 해서 오류가 발생했음.
    if p_a > p_b:
        parent[p_a] = p_b #parent[a] = p_b : 이런 식으로 해서 오류가 발생했음.


for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(a,b)
    elif cal == 1:
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")