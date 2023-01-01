import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for i in range(n):
    coin.append(int(input()))

# 동전의 종류를 내림차순 정렬
coin.sort(reverse=True)
# 횟수 변수
cnt = 0

# 큰 값부터 비교하여 계산
for i in coin:
    cnt += k // i
    k %= i
print(cnt)

# 전형적인 그리디 알고리즘 접근법
# 단 조건이 있기 때문에 가능! 꼭 조건 확인하자