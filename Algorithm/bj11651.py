import sys

num = int(sys.stdin.readline())
a = []
for i in range(num):
    x, y = map(int, sys.stdin.readline().split())
    # y 크기순으로 정렬
    grid = [y, x]
    a.append(grid)

a.sort()
for i in a:
    # 출력을 거꾸로
    print(i[1], i[0])