import sys
n = int(sys.stdin.readline())

# 비교대상
result = 1
for i in range(1,n+1):
    # num에 n값을 하나씩 나눠서 대입
    num = list(map(int, str(i)))

    # 분해합 변수 생성
    result = sum(num) + i

    # 분해합 연산 가능시 출력
    if n == result:
        print(i)
        break
    
    # 생성 불가능 시 0출력
    if n == i:
        print(0)
        break