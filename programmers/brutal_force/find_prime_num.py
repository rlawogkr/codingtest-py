from itertools import permutations

lst = [1,2,3]
perm = permutations(lst, 2)

for p in perm:
    print(p)