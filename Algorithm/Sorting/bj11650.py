import sys
n = int(input())

a = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    grid = [x, y]
    a.append(grid)
a.sort()
for i in a:
    print(i[0], i[1])