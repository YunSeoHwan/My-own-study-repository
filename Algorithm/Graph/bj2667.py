import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0

def dfs(x, y):
    global cnt
    visit[x][y] = True

    if graph[x][y] == 1:
        graph[x][y] = cnt + 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if (0 <= nx < n) and (0 <= ny < n):
            # 방문 되었는지
            if visit[nx][ny] == False:
                # 그래프 값이 0 인지
                if graph[nx][ny] == 0:
                    visit[nx][ny] = True

                else:
                    dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if visit[i][j] == False and graph[i][j] != 0:
            dfs(i, j)
            cnt += 1

print(cnt)

num = []
for i in range(cnt):
    c = 0
    for k in graph:
        c += k.count(i+1)
    num.append(c)
num.sort()
for i in num:
    print(i)