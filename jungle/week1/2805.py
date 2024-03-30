import sys

input = sys.stdin.readline

#높이 H를 지정.
#나무를 필요한 만큼만 집으로 가져가려고 한다.
#적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값?

n, m = map(int, input().rstrip().split()) #n: 나무의 수, m: 가져갈려는 나무 길이
tree = sorted([int(i) for i in input().rstrip().split()])

#[10, 15, 17, 20]
#최대값: max(tree) 최소값: 0
def sum_tree(lst, h):
    val = 0
    for i in lst:
        if i - h <= 0: val += 0
        else: val += (i-h)
    return val

def binary_search(tree, min, max):

    while min <= max:
        mid = (min + max) // 2
        if sum_tree(tree, mid) > m: min = mid + 1
        elif sum_tree(tree, mid) < m: max = mid -1
        else: return mid
    return max


print(binary_search(tree, 0, tree[len(tree)-1]))