import sys

n, m = map(int, sys.stdin.readline().split())
# 듣도 못한사람
listen = set()
# 보도 못한사람
look = set()

for i in range(n):
    listen.add(sys.stdin.readline().rstrip())

# 듣도 못한사람 list에 있을때만 추가
for i in range(m):
    look.add(sys.stdin.readline().rstrip())

# 듣도보다 못한 사람
aaa = list(listen & look)

# 알바벳순 정렬 후 출력
aaa.sort()
print(len(aaa))
for i in aaa:
    print(i)