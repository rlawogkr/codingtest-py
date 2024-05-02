import sys

def input():
    return sys.stdin.readline().rstrip()

#1.청소되지 않은 경우, 현재 칸을 청소
#2.청소되지 않은 빈 칸이 없는 경우 -> 바라보는 방향을 유지한 채 한 칸 후진 가능? 후진하고 1번으로
#2.청소되지 않은 빈 칸이 없는 경우 -> 바라보는 방향의 뒤쪽 칸이 벽, 후진할 수 없으면 작동을 멈춤.

#3.현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있을 경우?
# - 반시계 방향으로 90도 회전
# - 청소되지 않은 경우 한 칸으로 전진
# 1번으로 돌아감.
N, M = map(int, input().split())
r, c, d = map(int, input().split()) # (r,c) 청소기가 바라보는 방향.
#d:0[북] d:1[동] d:2[남] d:3[서]
#청소기가 있는 곳은 항상 빈칸.
graph = [list(map(int, input().split())) for _ in range(N)]