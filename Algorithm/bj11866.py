import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
# queue 생성
x = deque([])

# 정답 리스트
answer = []
for i in range(n):
    x.append(i+1)
while len(x) != 0:
    # k-1개 요소를 뒤로 삽입
    for i in range(k-1):
        a = x.popleft()
        x.append(a)
    # 젤 앞 요소 삽입후 제거
    answer.append(x[0])
    x.popleft()
a = str(answer)
a = a.replace('[', '<')
a = a.replace(']', '>')
print(a)