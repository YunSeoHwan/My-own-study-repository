import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(m)]

# queue 생성
queue = deque([])

# 방향 변수 생성 (왼, 오, 아래, 위)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 날짜 변수
day = 0

# 익은 토마토만 queue에 담음
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            queue.append([i, j])

# bfs
def bfs():
    while queue:

        # 첫 토마토 위치 pop
        x, y = queue.popleft()

        # 주변 토마토 익히는 과정
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            # matrix범위를 벗어나지 않으면서, 익지 않은 토마토여야함
            if 0 <= nx < m and 0 <= ny < n and tomato[nx][ny] == 0:
                # 해당 위치 1 더하기 -> 각 변화마다 day 카운팅
                # tomato배열에서 가장 큰 값이 day
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])

bfs()

# 모든 토마토 확인
for i in tomato:
    for j in i:

        # 익지 않은 토마토 존재하면 -1
        if j == 0:
            print(-1)
            exit(0)
    
    # 다 익었을 경우
    day = max(day, max(i))

# 첫 시작일수 빼기
print(day - 1)