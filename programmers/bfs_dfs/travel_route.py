tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# return ["ICN", "JFK", "HND", "IAD"]

def solution(tickets):
    city = {}
    tickets.sort() #사전 순, 오름차순 정렬
    #dict 세팅
    for ticket in tickets:
        if ticket[0] not in city:
            city[ticket[0]] = {}
            city[ticket[0]].put(ticket[1])
        else:
            city[ticket[0]].put(ticket[1])

    start = 'ICN'
    dfs(start, city, tickets)
    return city
def dfs(start, city, tickets):
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in city:
            break
        stack.append(city[node].pop())

