#나만의 L4 만들기

#라운드 로빈 방식: 1번 서버부터 시작, 1,2,...N,그리고 다시 1,2,...N
#sticky 옵션이 true인 경우, 이전에 분배된 서버로 요청이 배분되어야 함.
def solution(servers, sticky, requests):
    answer = [[]]
    return answer