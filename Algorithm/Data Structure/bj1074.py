import sys

input = sys.stdin.readline
n, c, r = map(int, input().split())

cnt = 0

while n != 0:

    n -= 1

    # 1사분면
    if c < pow(2, n) and r < pow(2, n):
        cnt += pow(2, n) * pow(2, n) * 0
    
    # 2사분면
    elif c < pow(2, n) and r >= pow(2, n):
        cnt += pow(2, n) * pow(2, n) * 1
        r -= pow(2, n)
    
    # 3사분면
    elif c >= pow(2, n) and r < pow(2, n):
        cnt += pow(2, n) * pow(2, n) * 2
        c -= pow(2, n)
    
    # 4사분면
    else:
        cnt += pow(2, n) * pow(2, n) * 3
        c -= pow(2, n)
        r -= pow(2, n)
print(cnt)

# 메모리 초과
# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10000)
# n, c, r = map(int, input().split())
# matrix = [[0] * pow(2,n) for _ in range(pow(2,n))]

# cnt = 0
# def z(n, x, y):

#     global cnt
#     real_y = y
#     if n == 1:
#         for _ in range(pow(2, n)):
#             for _ in range(pow(2, n)):
#                 matrix[x][y] = cnt
#                 y+=1
#                 cnt+=1
#             x+=1
#             y = real_y
#         return

#     else:
#         z(n-1, x, y)
#         z(n-1, x, y + pow(2,n-1))
#         z(n-1, x + pow(2, n-1), y)
#         z(n-1, x + pow(2, n-1), y + pow(2, n-1))

# z(n, 0, 0)
# print(matrix[c][r])