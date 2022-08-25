import sys

k, n = map(int, sys.stdin.readline().split())
lan = []
for _ in range(k):
    a = int(sys.stdin.readline())
    lan.append(a)

# 이분탐색 시작, 끝 설정
start, end = 1, max(lan)

while start <= end:

    mid = (start + end) // 2
    s = 0
    for i in lan:
        if i // mid !=0:
            s += (i//mid)

    if s < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)