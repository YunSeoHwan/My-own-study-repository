n = int(input())
stairs = [0]
# 최대값 저장
dp = [0] * (n+1)

for _ in range(n):
    stairs.append(int(input()))

# 계단 순서랑 일치
for i in range(1, n+1):
    if i == 1:
        dp[i] = stairs[1]
    elif i == 2:
        dp[i] = stairs[1] + stairs[2]
    elif i == 3:
        dp[i] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    else:
        dp[i] = max(stairs[i] + dp[i-2], stairs[i] + dp[i-3] + stairs[i-1])
print(dp[i])