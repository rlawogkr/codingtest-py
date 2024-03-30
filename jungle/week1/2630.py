#종이 자르는 규칙

#모두 같은 색으로 안칠해져 있으면 -> 가로. 세로로 중간부분을 자름
#더 이상 자를 수 없을 때까지 나눔.
#잘라진 하얀색 색종이와 파란색 색종이의 개수
import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = [list(map(int,input().rstrip().split())) for _ in range(n)]

def solution(y, x, n) :
  color = arr[y][x]
  for i in range(y, y+n) :
    for j in range(x, x+n) :
      if color != arr[i][j] :
        solution(y, x, n//2)
        solution(y, x+n//2, n//2)
        solution(y+n//2, x, n//2)
        solution(y+n//2, x+n//2, n//2)
        return
  if color == 0 :
    arr.append(0)
  else :
    arr.append(1)


solution(0,0,n)
print(arr.count(0))
print(arr.count(1))