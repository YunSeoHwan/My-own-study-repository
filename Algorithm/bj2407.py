import sys

input = sys.stdin.readline

n, m = map(int, input().split())

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

print(int(fact(n) // (fact(n-m) * fact(m))))