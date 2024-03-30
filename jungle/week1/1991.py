#트리 순회
import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    parent, left, right = input().rstrip().split()
    tree[parent] = [left, right] 

print(tree)
#전위 순회
def pre_order(root):
    if root != '.':
        print(root, end="")
        pre_order(tree[root][0]) #left
        pre_order(tree[root][1]) #right

#중위 순회
def in_order(root):
    if root != '.':
        in_order(tree[root][0]) #left
        print(root, end="")
        in_order(tree[root][1]) #right

#후위 순회
def post_order(root):
    if root != '.':
        post_order(tree[root][0]) #left
        post_order(tree[root][1]) #right
        print(root, end="")

pre_order('A')
print()
in_order('A')
print()
post_order('A')