import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# 그래프 생성
graph = [list(map(int, input().split())) for _ in range(n)]

# 출력할 행렬 생성
matrix = [[0] * n for _ in range(n)]

# BFS 
def bfs(start):
    
    # 시작노드를 Queue에 삽입
    queue = deque([start])

    # 방문처리 배열
    visit = [0 for _ in range(n)]

    while queue:
        v = queue.popleft()

        # 방문되지 않았으면서, 1이면 방문처리 후, 해당 노드 queue 삽입
        for i in range(n):
            if visit[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visit[i] = 1
                matrix[start][i] = 1

for i in range(n):
    bfs(i)

# 출력
for i in matrix:
    print(*i)

# 플로이드 - 워셜 방식
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):

            # i -> k -> j K를 거쳐 도달 가능하면 1
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for g in graph:
    print(*g)