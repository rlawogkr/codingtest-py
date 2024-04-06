import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
#st시간, en시간. 회의 최대 개수
room = [tuple(map(int, input().split())) for _ in range(N)]

sorted_room = sorted(room, key = lambda x: (x[1],x[0]))

end_time = sorted_room[0][1]
cnt = 1
for i in range(1, len(sorted_room)):
    if end_time > sorted_room[i][0]:
        continue
    #시작점이 끝지점보다 크거나 같을 때
    else:
        cnt += 1
        end_time = sorted_room[i][1]

print(cnt)