# dfs bfs
import sys
from collections import deque

# node, 간선, 시작위치
n, m, v = map(int, sys.stdin.readline().split())

# 방문 리스트
visited = [0] * (n+1)
graph = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):

    # 시작노드 방문
    visited[v] = 1
    print(v, end=' ')

    # node 숫자부터 보기위해 1부터 반복
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    # 시작노드 queue에 삽입
    queue = deque([v])

    # dfs에서 1로 되었기 때문에 0 처리
    visited[v] = 0

    # queue가 빌때까지
    while queue:

        # queue 첫번째 요소 반환
        v = queue.popleft()
        print(v, end=' ')

        # 방문되지 않은 인접노드 queue에 넣고 방문처리
        for i in range(1,n+1):
            if visited[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 0
dfs(v)
print()
bfs(v)