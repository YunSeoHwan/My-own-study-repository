# 팩토리얼 함수 정의
def fact(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

a, b = map(int, input().split())

result = fact(a) / fact(b) / fact(a-b)
print(int(result))