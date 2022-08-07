from collections import deque
import sys
que = deque([])

x = int(sys.stdin.readline())
for i in range(x):
    y = sys.stdin.readline().split()
    if y[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            a = que.popleft()
            print(a)
    elif y[0] == 'push':
        que.append(int(y[1]))
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