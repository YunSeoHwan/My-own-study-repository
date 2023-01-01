import sys

# 재귀 허용 깊이
sys.setrecursionlimit(10 ** 6)

n,m,r = map(int, sys.stdin.readline().split())

# index번호와 같게하기 위해 n+1
graph = [[] for _ in range(n+1)]
# 방문노드
visited = [0] * (n+1)
cnt = 1
def reculsive_dfs(v):
    global cnt

    visited[v] = cnt
    for i in graph[v]:
        if visited[i] == 0:
            cnt+=1
            reculsive_dfs(i)
# 노드 입력받기
for i in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 오름차순 정리
for i in range(n+1):
    graph[i].sort()

reculsive_dfs(r)

for i in range(n+1):
    if i!=0:
        print(visited[i])