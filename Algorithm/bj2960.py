# 에라토스테네스의 체
import sys

n, k = map(int, sys.stdin.readline().split())

# True 배열 생성 -> index가 1 작음으로 n+1개 생성
num = [True] * (n+1)

# 지워지는 순서
count = 1

for i in range(2, n+1):
    # False로 바뀌지 않았을때만
    if num[i] == True:
        for j in range(i, n+1, i):

            # 이미 False면 계속 진행
            if num[j] == False:
                continue
            
            if count == k:
                print(j)

            num[j] = False
            count += 1