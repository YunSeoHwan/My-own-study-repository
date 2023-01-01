import sys
import heapq

n = int(input())
heap = []

for _ in range(n):

    element = int(sys.stdin.readline())

    # 원소 삭제
    if element == 0:
        # heap이 비었을 때, 0 출력
        if len(heap) == 0:
            print(0)
        # heap은 최소힙을 지원함으로 -1을 곱하여 최대힙 구현
        else:
            print((-1)*heapq.heappop(heap))

    # 원소 추가
    else:
        heapq.heappush(heap, (-1)*element)