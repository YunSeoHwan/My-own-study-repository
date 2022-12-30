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
        # 최소값 출력 -> o(1) heap[0]에 위치함
        else:
            print(heapq.heappop(heap))

    # 원소 추가
    else:
        heapq.heappush(heap, element)