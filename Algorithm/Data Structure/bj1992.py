import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())

# 배열
matrix = [list(map(int, input().strip())) for _ in range(n)]

# 출력 배열
cnt = []

# 분할정복
def sol(x, y, n):

    # 해당 좌표값 설정
    grid = matrix[x][y]

    # 해당 값과 모든 행렬이 동일한지 비교
    for i in range(x, x + n):
        for j in range(y, y + n):

            # 다르다면 분할정복
            if grid != matrix[i][j]:

                # 괄호 추가
                cnt.append('(')
                sol(x, y, n//2)
                sol(x, y + n//2, n//2)
                sol(x + n//2, y, n//2)
                sol(x + n//2, y + n//2, n//2)
                # 모든 재귀 종료 후 괄호 닫기
                cnt.append(')')
                return

    # 1로만 채워지면 1 추가, 그렇지 않으면 0
    if grid == 1:
        cnt.append('1')
    else:
        cnt.append('0')

# 출력
sol(0, 0, n)
for i in cnt:
    print(i, end='')