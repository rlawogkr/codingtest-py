from itertools import combinations

n = int(input())
for comb in combinations(range(0, n), n // 2):
    a_team = list(comb)
    b_team = [i for i in range(0, n) if i not in a_team]

    print(a_team)
    print(b_team)
