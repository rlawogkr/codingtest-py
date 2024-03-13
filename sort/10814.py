import sys

input = sys.stdin.readline


N = int(input())
people = [[[] for _ in range(2)] for _ in range(N)]

for i in range(N):
    people[i][0], people[i][1] = input().split()
    people[i][0] = int(people[i][0])
res = sorted(people, key = lambda obj: obj[0])
_list = []
for i in res:
    _list.append(str(i[0])+" "+i[1])
    
print("\n".join(_list))


