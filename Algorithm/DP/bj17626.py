import sys

input = sys.stdin.readline

n = int(input())

# dp 생성
dp = [0] * (n+1)

for i in range(1, n+1):

    # 최대값 생성
    min_num = sys.maxsize

    # 1일때는 1제곱
    if i == 1:
        dp[i] = 1
    
    # 제곱수는 root만큼 비교하면 됨
    else:
        for j in range(1, int(i ** 0.5) + 1):
            min_num = min(min_num, dp[i - (j ** 2)])
        dp[i] = min_num + 1

print(dp[n])