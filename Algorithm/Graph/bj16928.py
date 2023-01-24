import sys
from collections import deque

input = sys.stdin.readline

# 1 ~ 100번 칸 방문횟수
matrix = [0] * 101

# 방문 여부
visited = [False] * 101

# 사다리, 뱀 갯수 입력
n, m = map(int, input().split())

ladder = dict()
snake = dict()

for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

def bfs():
    queue = deque([1])

    while queue:
        v = queue.popleft()

        # 100에 도착하면 방문횟수 출력
        if v == 100:
            print(matrix[v])
            break

        for dice in range(1, 6):
            # 다음 이동할 위치
            place = dice + v
            
            # 범위안에서 방문되지 않았다면
            if place <= 100 and visited[place] == False:
                
                # 사다리를 만났다면 위치변경
                if place in ladder.keys():
                    place = ladder[place]
                
                # 뱀을 만났다면 위치변경
                if place in snake.keys():
                    place = snake[place]
                
                # 뱀과 사다리가 없다면, 방문처리
                if visited[place] == False:
                    visited[place] = True
                    matrix[place] = matrix[v] + 1
                    queue.append(place)

bfs()