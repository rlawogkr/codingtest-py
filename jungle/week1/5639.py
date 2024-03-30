import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
#왼쪽 서브트리에 있는 노드키는 노드키보다 작다
#오른쪽 서브트리에 있는 노드키는 노드키보다 작다

#전위순회: 루트, 왼쪽, 오른쪽
arr = []
while True:
    try: 
        val = int(input().rstrip())
        arr.append(val)
    except:
        break
    
left_arr = []
right_arr = []
def binary_search_tree(arr):
    global left_arr, right_arr
    
    val = arr[0]
    for i in range(1, len(arr)-1):
        # 제일 왼쪽 지점보다 값이 큰 인덱스
        if arr[i] > val:
            left_arr = arr[1:i] 
            right_arr = arr[i:]
            break
        #모두 그 값보다 작은 경우
        else:
            left_arr = arr[1:]

    binary_search_tree(left_arr)
    binary_search_tree(right_arr)
    print(val)

binary_search_tree(arr)