def dp(n):
    cnt = [0] * (n+1)
    
    for i in range(1, n+1):
        if i == 1:
            cnt[i] = 1
        elif i == 2:
            cnt[i] = 3
        else:
            cnt[i] = cnt[i-1] + 2*cnt[i-2]

    print(cnt[i] % 10007)
n = int(input())
dp(n)