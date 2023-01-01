import sys
def dp(n):
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 15746
    print(dp[i])
n = int(sys.stdin.readline())
dp(n)

# n이 100만 이상이면 출력에서 나머지출력시 값이 굉장히 커짐
# 미리 나누는 습관