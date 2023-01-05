import sys

input = sys.stdin.readline
t = int(input())

def fact(n):
    res = [1] * (n+1)
    for i in range(1, n+1):
        if i == 1:
            res[i] = 1
        elif i == 2:
            res[i] = 2
        else:
            res[i] = res[i-1] * i

    return res[n]

for _ in range(t):
    n, m = map(int, input().split())
    res = fact(m) // (fact(n) * fact(m-n))
    print(int(res))