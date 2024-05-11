#5607. [Professional] 조합
from math import factorial

tc = int(input())
for t in range(tc):
    n, r = map(int, input().split())
    print(f'#{t+1} {factorial(n)//(factorial(r)*factorial(n-r))}')