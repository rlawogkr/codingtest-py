'''
가짜 영수증 판별하기. 가짜 영수증에는 금액이 옳지 않게 적혀있음.

옳은 금액?
0~9 사이의 숫자 또는 ,로만 구성.
금액이 0원인 경우를 제외하고는 가장 왼쪽 숫자가 0일 수 없음. 0100은 옳지 않음.
금액은 세자리 구분자(,)를 포함하고 있거나, 전혀 포함하지 않음. 39900도 옳은 금액.
세자리 구분자: 가장 오른쪽 숫자부터 시작해 왼쪽 방향으로 3개의 숫자바다 1개의 ,가 나타남.
25,000,123은 옳은 금액. 24,999,99는 옳지 않은 금액.
가장 왼쪽 끝이나 오른쪽 끝에는 ,가 나타나지 않음.

amountText가 옳은 금액이면 True, 아니면 False를 반환.

'''

def solution(amountText):
    answer = True
    n = len(amountText)
    if amountText[0] == ',' or amountText[-1] == ',':
        return False

    for i in range(n):
        if not amountText[i].isdigit() and amountText[i] != ',':
            answer = False
            break
    if amountText[0] == '0' and len(amountText) > 1:
        answer = False
    if amountText.count(',') >= 1:
        comma_positions = range(n-4, 0, -4)
        for pos in comma_positions:
            if amountText[pos] != ',':
                answer = False
                break
    return answer