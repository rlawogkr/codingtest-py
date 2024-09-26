# 재귀 check

adj_list = [[1, 2], [3, 4], [5, 6], [7], [8], [], [9], [], [], [10], []]
info = [0,1,0,1,1,0,1,0,0,1,0]
def dfs(cur_idx, visited, adj_list, info):
    cur_sheep = 0
    cur_wolf = 0
    visited[cur_idx] = True

    for next_idx in adj_list[cur_idx]:
        if not visited[next_idx]:
            if info[next_idx] == 0:
                cur_sheep += dfs(next_idx, visited, adj_list, info)[0]
            else:
                cur_wolf += dfs(next_idx, visited, adj_list, info)[1]

    if info[cur_idx] == 0:
        cur_sheep += 1
    else:
        cur_wolf += 1

    return cur_sheep, cur_wolf



