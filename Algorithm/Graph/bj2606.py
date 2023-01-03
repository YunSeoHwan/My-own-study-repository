import sys
from collections import deque

# node, 간선, 시작위치
n = int(sys.stdin.readline())
node = int(sys.stdin.readline())

# 방문 리스트
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

# 인접 노드 구현
for i in range(node):
    a, b = map(int, sys.stdin.readline().split())

    # 연결 노드는 각 배열에 할당 ex) [[], [2], [1], []]
    graph[a].append(b)
    graph[b].append(a)

print(graph)

# dfs 재귀 구현
def dfs(v):

    # 방문처리
    visited[v] = 1

    # 방문처리 되지 않았으면 재귀
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

# dfs stack 구현
def dfs_stack(v):

    # 스택생성
    stack = [v]

    # 스택 empty 때까지
    while stack:

        s = stack.pop()

        # 방문되지 않았으면 방문처리
        if visited[s] == 0:
            visited[s] = 1

            # 해당 노드 연결요소 stack에 삽입
            for w in graph[s]:
                stack.append(w)

# bfs 구현
def bfs(v):
    
    # 방문처리
    visited[v] = 1

    # 큐 생성
    queue = deque([v])

    # 큐가 empty때 까지
    while queue:

        # 먼저 삽입된 노드 pop
        q = queue.popleft()

        # q와 연결된 모든 요소 확인
        for i in graph[q]:
            
            # 방문되지 않은 노드는 queue에 삽입 후, 방문처리
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                
dfs(1)
dfs_stack(1)
bfs(1)

# 1에서 시작임으로 1제외하고 출력
print(visited.count(1)-1)