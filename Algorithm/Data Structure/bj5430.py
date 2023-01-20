import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    
    # reverse check
    flag = False

    # 함수 list
    f = list(map(str, input().strip()))

    # 배열 크기
    num = int(input())
    
    # 덱에 배열 삽입
    queue = deque(input().rstrip()[1:-1].split(","))

    # 배열크기가 0이면 빈 덱 생성
    if num == 0:
        queue = deque()

    for j in f:
        # R일때, flag 변경
        if j == 'R':
            if flag == True:
                flag = False
            else:
                flag = True

        # 삭제
        elif j == 'D':
            # 빈 배열 아닐때, flag유무로 삭제
            if len(queue) != 0:
                if flag == True:
                    queue.pop()
                elif flag == False:
                    queue.popleft()

            # 비었다면 error
            else:
                print('error')
                break
                
    else:
        if flag == False:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")