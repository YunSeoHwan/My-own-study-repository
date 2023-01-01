import sys

# 브루트포스에 대해 알자
n = int(sys.stdin.readline())
cnt = 0
six_n = 666
while True:
    # 666이 나오면 카운트
    if '666' in str(six_n):
        cnt += 1
    # 카운트와 n 일치시 숫자 출력
    if cnt == n:
        print(six_n)
        break
    six_n += 1