tc = int(input())

# 해당 영역 안에 존재하는 파리의 개수
# M*M 크기의 파리채를 내려쳐 최대한 많은 파리 죽이기
# 죽은 파리 개수 구해라
def kill(graph, x, y): # x,y는 시작점
    killed = 0
    for i in range(x, x+m):
        for j in range(y, y+m):
            killed += graph[i][j]
    return killed

for i in range(1, tc+1):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    max_val = -int(1e9)
    for x in range(n-m+1):
        for y in range(n-m+1):
            max_val = max(max_val,kill(graph, x, y))

    print("#{} {}".format(i, max_val))