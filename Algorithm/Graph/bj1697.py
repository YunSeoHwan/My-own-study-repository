import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

# 걸린시간 리스트
visit = [0 for _ in range(100001)]

def bfs(n):
    # 큐 생성
    q = deque()
    q.append(n)

    # 시작위치 1 표시
    visit[n] = 1

    while q:
        # 큐에서 원소 pop
        c = q.popleft()

        # k와 같다면 -1 하고 출력 -> 시작을 1로 했기 때문
        if c == k:
            print(visit[c] - 1)
            return
        
        # 순간이동, 일반이동 고려
        for i in (c-1, c+1, c*2):

            # 범위내에 있다면, 해당노드 걸린시간 +1
            if 0 <= i <= 100000 and not visit[i]:
                visit[i] = visit[c] + 1
                q.append(i)
bfs(n)