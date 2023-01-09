import sys
import heapq

input = sys.stdin.readline

max_heap = [1]       # 최대힙
min_heap = []       # 최소힙

visit = [False] * 1_000_001     # 방문 처리, False = 삭제, True = 미삭제

n = int(input())

for _ in range(n):

    t = int(input())
    for i in range(t):

        # 연산과 원소 받음
        op, num = map(str, input().split())
        num = int(num)

        # input 일때
        if op == 'I':

            # 최대힙, 최소힙에 index번호와 함께 삽입
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, ((-1)*num, i))

            # 원소있음, 미삭제 처리
            visit[i] = True
        
        # delete 일때
        elif op == 'D':
            
            # 최소값 삭제
            if num == -1:
                
                # 상대힙에 의해 삭제되었을 경우, 해당원소 계속해서 삭제
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                
                # 배열안에 원소 존재시, 삭제처리하고 pop
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            
            elif num == 1:
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    # 삭제처리가 되지 않은 원소들 삭제
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # heap에 원소가 존재할 경우, 최대, 최소값 출력
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')

# import sys
# import heapq

# input = sys.stdin.readline
# heap = []

# n = int(input())
# for _ in range(n):

#     t = int(input())
#     for _ in range(t):
#         op, num = map(str, input().split())
#         num = int(num)

#         if op == 'I':
#             # heapq.heappush(heap, num)
#             heap.append(num)
        
#         elif op == 'D':

#             if num == 1:
#                 heapq.heapify(heap)
#                 if len(heap) != 0:
#                     heap.remove(heap[len(heap) - 1])

#             elif num == -1:
#                 heapq.heapify(heap)
#                 if len(heap) != 0:
#                     heap.remove(heap[0])

#     if len(heap) == 0:
#         print('EMPTY')
    
#     else:
#         print(max(heap), min(heap))