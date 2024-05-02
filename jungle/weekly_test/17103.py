#골드바흐의 추측
# 문제: 2보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
import sys
def input():
    return sys.stdin.readline().rstrip()
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

total_prime_lst = prime_list(1000001) #모든 prime 값


T = int(input())
res = []

for _ in range(T):
    n = int(input())
    cnt = 0
    for i in total_prime_lst[:]:
        if n-i < i: break
        if n-i in total_prime_lst:
            cnt += 1
    res.append(cnt)

print("\n".join(map(str, res)))
