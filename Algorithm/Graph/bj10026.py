import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())

# 그래프 저장
graph = [list(input().rstrip()) for _ in range(n)]

# 방문여부 판단
visited = [[False] * n for _ in range(n)]

# DFS
def dfs(x, y, color):

    # 범위를 벗어나면 False
    if x >= n or x <= -1 or y >= n or y <= -1:
        return False

    # 이미 방문된 노드라면 False
    if visited[x][y] == True:
        return False

    # 현재위치 color 저장
    c = graph[x][y]

    # 현재위치와 인접노드의 색이 동일할 때
    if color == c:
        
        # 방문처리 후, 상하좌우
        visited[x][y] = True
        dfs(x-1, y, c)
        dfs(x, y-1, c)
        dfs(x+1, y, c)
        dfs(x, y+1, c)
        return True

    return False

# 정상, 색맹 변수
normal, abnormal = 0

# 정상 카운팅
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            if dfs(i, j, graph[i][j]) == True:
                normal +=1

# G를 R로 교체, 방문배열 초기화
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
        visited[i][j] = False

# 색맹 카운팅
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            if dfs(i, j, graph[i][j]) == True:
                abnormal +=1  

# 출력
print(normal, abnormal)