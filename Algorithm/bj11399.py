import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))

k.sort()
s = 0
real = 0
for i in k:
    s = s + i
    real += s
    print(s)
print(real)