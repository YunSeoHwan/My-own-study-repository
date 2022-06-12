num = int(input())

for i in range(num):
    k = int(input())
    n = int(input())
    apart = [i for i in range(1, n+1)]          # 한줄 반복문 확인하기

    for i in range(k):
        for j in range(1, n):
            apart[j] += apart[j-1]
    print(apart[-1])                            # 조합 combination 방법