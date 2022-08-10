import sys

n = int(sys.stdin.readline())
# 키, 무게 list
data = []
# 등수 list
rank = []

# 키, 무게 저장
for i in range(n):
    w, h = map(int, sys.stdin.readline().split())
    data.append((w,h))

# 값 하나씩 비교하며 자신보다 큰 사람 있을시 +1
for i in range(n):
    count = 1
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    rank.append(count)
for i in rank:
    print(i, end=" ")