import sys
def dp(n):
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if i == 1 or i == 2 or i == 3:
            dp[i] = 1
        else:
            dp[i] = dp[i-2] + dp[i-3]
    print(dp[i])
n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    dp(m)