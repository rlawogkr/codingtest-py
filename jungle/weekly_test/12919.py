import sys

def input():
    return sys.stdin.readline().rstrip()

# s를 이용해서 t를 만들 수 있는지 체크
s = list(input())
t = list(input())
def sort_list(lis):
    res = []
    for i in range(len(lis)-1, -1, -1):
        res.append(lis[i])
    return res

def operand(s, i):
    if i == 0:
        s.append('A')
    else:
        s.append('B')
        sort_list(s)
def make_t(s, t):
    if len(s) == len(t):
        if s == t:
            return 1

    for i in range(2):
        operand(s, i)
        if len(s) <= len(t):
            make_t(s,t)
            if i == 0:
                s.pop()
            else:
                s.pop()