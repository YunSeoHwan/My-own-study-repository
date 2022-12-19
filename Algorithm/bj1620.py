import sys

n, m = map(int, sys.stdin.readline().split())

# 딕셔너리 생성
poket = {}

# 각각의 key, value 다 생성
for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    poket[i] = name
    poket[name] = i

for i in range(m):
    quiz = sys.stdin.readline().rstrip()
    if quiz.isdigit():
        print(poket[int(quiz)])
    else:
        print(poket[quiz])