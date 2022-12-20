import sys

# dp 이용
def dp(n):

    # 합 개수를 담을 리스트
    sum_case = [0] * (n+1)

    # n을 index로 사용하기 위해 1부터 시작
    for i in range(1,n+1):
            
        if i == 1:
            sum_case[i] = 1
        elif i == 2:
            sum_case[i] = 2
        elif i == 3:
            sum_case[i] = 4
        else:
            sum_case[i] = sum_case[i-1] + sum_case[i-2] + sum_case[i-3]
        
        # 해당 값 출력
        if i == n:
            print(sum_case[i])

n = int(sys.stdin.readline())
for i in range(1, n+1):
    num = int(sys.stdin.readline())
    dp(num)