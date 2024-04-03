# 이진 검색 트리
# 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과 출력.
import sys
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()


def postorder(start, end):
    if start > end:
        return
    div = end+1
    for i in range(start+1, end+1):
        if arr[start] < arr[i]:
            div = i
            break
        
    postorder(start+1, div-1)
    postorder(div, end)
    print(arr[start])

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break
postorder(0, len(arr)-1)