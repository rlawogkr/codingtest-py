# 뱀 길이: 1, N*N 정사각 보드 위에서 진행. 몇몇 칸에는 사과가 있음.
#뱀 위치 시작점: 좌상단. 처음에는 뱀이 오른쪽을 향함.

import sys

input = sys.stdin.readline

n = int(input().rstrip())
dy, dx = [0,1,0,-1], [1,0,-1,0] #우, 하, 좌, 상

apple_count = int(input().rstrip())
apple_list = []
for _ in range(apple_count):
    apple_list.append(tuple(map(int,input().rstrip().split())))

# [0, 0, 0, 'D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'L', 0, 'D' ...]
d_table = [0]*10001
dir_count = int(input().rstrip())
for _ in range(dir_count):
    time, dir = input().rstrip().split()
    d_table[int(time)] = dir


snake = [(1,1)]
answer = 0 # 0초
dr = 0 # 현재 방향

while True:
    answer += 1
    cur_y, cur_x = snake[0]
    new_y, new_x = cur_y + dy[dr], cur_x + dx[dr]

    if 1 <= new_y <= n and 1 <= new_x <= n and (new_y, new_x) not in snake:
        snake.insert(0, (new_y, new_x)) #가장 앞 부분에 변한 위치 넣기
        #사과를 만났을 경우
        if (new_y, new_x) in apple_list:
            apple_list.remove((new_y, new_x))
        #사과를 만나지 않았을 경우
        else:
            snake.pop()
        
        if d_table[answer] == 'D': dr = (dr + 1) % 4 #오른쪽 방향 전환
        elif d_table[answer] == 'L': dr = (dr + 3) % 4 #왼쪽 방향 전환
    else:
        break

print(answer)
            


