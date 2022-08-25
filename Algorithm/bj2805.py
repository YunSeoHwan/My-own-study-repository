import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    s = 0

    for i in tree:
        if i >=mid:
            s += (i-mid)
        
    if s >= m:
        start = mid + 1
    else:
        end = mid - 1

print(start)