from collections import deque
import sys
# 큐 생성
que = deque([])

x = int(sys.stdin.readline())
for i in range(x):
    # push x를 분리하기 위한 작업
    y = sys.stdin.readline().split()
    if y[0] == 'push_front':
        que.appendleft(int(y[1]))
    elif y[0] == 'push_back':
        que.append(int(y[1]))    
    elif y[0] == 'pop_front':
        a = que.popleft()
        print(a)
    elif y[0] == 'pop_back':
        a = que.pop()
        print(a)
    elif y[0] == 'size':
        print(len(que))
    elif y[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif y[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif y[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que) - 1])