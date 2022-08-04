import sys
n = int(sys.stdin.readline())

p = []
x = 0
y = 0
for i in range(n):
    h, w, m = map(int, sys.stdin.readline().split())
    if m % h == 0:
        x = h
        y = m // h
    else:
        x = m % h
        y = (m // h) + 1
    if y < 10:
        y = '0' + str(y)
    x = str(x)
    y = str(y)
    p.append(x+y)



for i in p:
    print(i)