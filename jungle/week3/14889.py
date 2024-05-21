#스타트링크
import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
#i,j 와 j,i는 같을 수 있음.
#스타트팀/링크팀의 능력치 차이를 최소로 하려고 함.
graph = [list(map(int, input().split())) for _ in range(N)]

min_val = int(1e9) # return값
#(1명, 5명) (2명, 4명) (3명, 3명) N:6
for j in range(1,N-1):
    for comb in combinations(range(0, N), j):
        start_team = list(comb)
        link_team = [i for i in range(0, N) if i not in start_team]
        s_val = 0
        l_val = 0
        for i in range(0,len(start_team)-1):
            for j in range(i+1, len(start_team)):
                s_val += (graph[start_team[i]][start_team[j]] + graph[start_team[j]][start_team[i]])
                l_val += (graph[link_team[i]][link_team[j]] + graph[link_team[j]][link_team[i]])
        min_val = min(abs(s_val - l_val), min_val)

print(min_val)
            
            
        