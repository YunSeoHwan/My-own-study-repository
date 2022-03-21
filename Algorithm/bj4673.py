start_num = set(range(1,10001))     # 1 ~ 10,000 숫자
remove_num = set()                  # 제거해야 할 생성자 -> 차집합으로 접근

for i in range(1,10001):
    for j in str(i):    # i 값을 하나씩 받음 ex) 723 -> 7, 2, 3
        i += int(j)     # int로 변환 후 더함
    remove_num.add(i)   # 제거 항목에 추가

self_num = set(start_num - remove_num)  # 구하고자 하는 값 (리스트끼리 빼기 안됨)

for i in sorted(self_num):  # 정렬 후 값 출력
    print(i)