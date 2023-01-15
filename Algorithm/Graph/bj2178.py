import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]

visit = [[False] * m for _ in range(n)]

# 상하좌우
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# BFS
def bfs(x, y):
    
    # Queue 생성
    queue = deque([])
    queue.append([x, y])

    while queue:

        # 가장 최근 값 pop
        x, y = queue.popleft()

        # 상하좌우
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            # 범위내에 존재하면서, 1인데 방문되지 않았으면
            if (0 <= nx < n) and (0 <= ny < m) and matrix[nx][ny] == 1:

                # 현재위치 + 1
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

# 출력               
bfs(0, 0)
print(matrix[n-1][m-1])