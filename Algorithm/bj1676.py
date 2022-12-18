import sys

# 팩토리얼 함수 (DP 이용)
def fact(n):
    array = []
    fact_array = [1] * (n+1)        # 각각의 fact값 저장
    for i in range(1, n+1):
        if n == 1:
            fact_array[1] = 1
        elif n == 2:
            fact_array[2] = 2
        else:
            fact_array[i] = i * fact_array[i-1]
    # n! 값 f에 할당
    f = fact_array[n]

    # 값 뒤에서 부터 끊어서 삽입
    while True:
        array.append(f % 10)
        f = f // 10
        if f == 0:
            break
    cnt = 0
    # 0이 안나오면 return
    for i in array:
        if i == 0:
            cnt +=1
        else:
            return cnt
n = int(sys.stdin.readline())
print(fact(n))

# 처음에 재귀함수로 호출해서 시간초과 발생
# DP를 이용하여 시간복잡도를 줄임. -> 앞으로 재귀호출은 가능한 DP이용