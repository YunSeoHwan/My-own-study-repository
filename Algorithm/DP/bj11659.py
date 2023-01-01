import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

# dp 이용
dp = [0] * (n+1)

# 각 구간까지의 합 저장
for i in range(1,len(num)+1):
    if i == 1:
        dp[i] = num[i-1]
    else:
        dp[i] = dp[i-1] + num[i-1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    # 구간 빼기
    print(dp[j] - dp[i-1])