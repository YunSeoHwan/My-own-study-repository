import sys

n = int(sys.stdin.readline())

square = []
for _ in range(n):
    square.append(list(map(int, sys.stdin.readline().split())))

# 색종이 색 count
blue = []
white = []

# 함수 정의
def solution(x, y, n):
    # 색종이 색 여부 판단
    color = square[x][y]

    # 색종이 색 판단
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 색깔이 다르면 분할
            if color != square[i][j]:
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    
    if color == 1:
        blue.append(1)
    else:
        white.append(1)

solution(0,0,n)
print(len(white))
print(len(blue))