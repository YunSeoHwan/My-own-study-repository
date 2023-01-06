import heapq
import sys

input = sys.stdin.readline
n = int(input())

# heap 저장 리스트
heap = []

for i in range(n):
    x = int(input())

    # x가 0이 아니면, 절댓값과 입력값 동시 저장
    # 절댓값을 우선적으로 정렬
    if x != 0:
        heapq.heappush(heap, [abs(x), x])
    
    # 0 입력의 경우
    else:

        # emtpy면 0 출력
        if len(heap) == 0:
            print(0)

        # 원래 heap 원소 출력
        else:
            print(heapq.heappop(heap)[1])