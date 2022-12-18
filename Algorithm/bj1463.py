n = int(input())

# dp 이용
dp = [0] * (n+1)

# i가 1이면 1이 나옴
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    # -1 한 경우와 비교해서 더 작은 경우 선택
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])

# 단순 조건, 반복문으로 접근해서 시간초과가 생겼다.
# dp 이용을 항상 참고!