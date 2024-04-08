import sys

def input():
    return sys.stdin.readline().rstrip()

#cctv는 방향에 있는 칸 전체를 감시할 수 있음.
#cctv는 벽을 통과할 수 없음.
#0: 빈칸, 6: 벽, 회전: 90도 방향
#1~5: cctv 번호.