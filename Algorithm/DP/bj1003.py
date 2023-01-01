import sys

# DP 이용
def fibo(n):
    zero_list = [0] *(n+1)
    one_list = [0] *(n+1)
    for i in range(n+1):
        if i == 0:
            zero_list[i] = 1
            one_list[i] = 0
        elif i == 1:
            zero_list[i] = 0
            one_list[i] = 1
        # 인덱스에 요소 카운트 횟수 저장
        else:
            zero_list[i] = zero_list[i-1] + zero_list[i-2]
            one_list[i] = one_list[i-1] + one_list[i-2]
    
    # n번째 count 횟수 반환
    return zero_list[n], one_list[n]

n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    a, b = fibo(m)
    print(a, b)