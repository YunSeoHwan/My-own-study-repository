import sys
from collections import deque
n = int(sys.stdin.readline())

# queue 생성
x = deque([])
for i in range(n):
    x.append(i+1)
while len(x) != 1:
    x.popleft()
    t = x.popleft()
    x.append(t)
print(x[0])