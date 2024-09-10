from collections import deque
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    result = [0 for i in range(m+1)] # 각 열의 땅의 개수를 저장할 리스트
    visited = [[0 for i in range(m)] for j in range(n)]
    def bfs(x, y):
        count = 0
        visited[x][y] = 1
        q = deque()
        q.append((x, y))
        min_y, max_y = 1e9, -1e9 #
        while q:
            curx,cury = q.popleft()
            min_y = min(min_y, cury)
            max_y = max(max_y, cury)
            count += 1
            for i in range(4):
                nx = curx + dx[i]
                ny = cury + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))

        for i in range(min_y, max_y+1):
            result[i] += count

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i,j)
    answer = max(result)
    return answer

# 첫 번째 테스트 케이스
print(solution([[0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0],
                [1, 1, 0, 0, 0, 1, 1, 0],
                [1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 1]]))  # 예상 결과: 9

# 두 번째 테스트 케이스
print(solution([[1, 0, 1, 0, 1, 1],
                [1, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 1],
                [1, 0, 0, 1, 0, 0],
                [1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1]]))  # 예상 결과: 16
