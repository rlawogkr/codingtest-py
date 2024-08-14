import sys
#. 16637. 괄호 추가하기
# 0~9, +, -, * 으로 이루어진 식
# 항상 올바른 수식만 주어짐
# 왼쪽부터 순차적으로 계산
# 괄호 안에는 연산자가 하나만 들어있어야 함 && 중첩된 괄호는 사용 불가
# 괄호를 추가하여 얻을 수 있는 식의 최댓값 구하기
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
exp = input()
ans = -sys.maxsize

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def dfs(idx, res):
    global ans
    if idx >= n:
        ans = max(ans, res)
        return

    # 괄호를 넣지 않는 경우
    if idx + 2 < n:
        next_res = calculator(res, int(exp[idx+2]), exp[idx+1])
        dfs(idx + 2, next_res)

    # 괄호를 넣는 경우
    if idx + 4 < n:
        # 괄호를 포함한 계산
        next_res = calculator(int(exp[idx]), int(exp[idx+2]), exp[idx+1])
        parenthesis_res = calculator(res, next_res, exp[idx-1])
        dfs(idx + 4, parenthesis_res)

# 첫 번째 숫자와 연산자를 기준으로 초기화
initial_res = int(exp[0])
dfs(2, initial_res)
print(ans)


