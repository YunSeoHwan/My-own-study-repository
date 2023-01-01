import sys

# node, 간선, 시작위치
n = int(sys.stdin.readline())
node = int(sys.stdin.readline())

# 방문 리스트
visited = [0] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]

# 인접 노드 구현
for i in range(node):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

# dfs 구현
def dfs(v):

    # 방문처리
    visited[v] = 1

    # node 접근 변수
    j = 0

    for i in graph[v]:
        # 연결 되었으면, 0으로 처리하고 dfs
        if i == 1:
            graph[v][j] = 0
            graph[j][v] = 0
            dfs(j)
        j+=1

dfs(1)
# 1에서 시작임으로 1제외하고 출력
print(visited.count(1)-1)