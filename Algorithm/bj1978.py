# 소수찾기 알고리즘
import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

# 갯수
count = 0
for i in num:
    cnt = 0
    if i == 1:
        continue

    # 나머지가 0이 나오는 경우가 1번이면 소수
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
        
    if cnt == 1:
        count +=1
print(count)