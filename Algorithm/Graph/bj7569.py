import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

day = 0

queue = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                queue.append([i, j, k])

# 이동변수
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        
        # x, y, z 할당
        z, y, x = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            # 범위내에 존재하면서 익지않은 토마토 만나면 1 증가
            if 0 <= nx < m and 0 <= ny < n and  0 <= nz < h and matrix[nz][ny][nx] == 0:
                matrix[nz][ny][nx] = matrix[z][y][x] + 1
                queue.append([nz, ny, nx])
bfs()

# 모든 토마토 확인
for i in range(h):
    for j in range(n):
        for k in range(m):

            # 익지 않은 토마토 존재하면 -1
            if matrix[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                # 최대일수 저장
                day = max(day, matrix[i][j][k])

# 첫 시작일수 빼기
print(day - 1)