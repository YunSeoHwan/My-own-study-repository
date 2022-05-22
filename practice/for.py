# 1
meau = ['김밥', '라면', '튀김']
for m in meau:
    print('오늘의 메뉴 : ', m)

# 2
stock = ['SK하이닉스', '카카오', '삼성전자']
for s in stock:
    print(len(s))                       # 6 3 4

# 3
lang = ['a', 'b', 'c', 'd']
for l in lang[1:]:
    print(l)                            # b c d
print()

# 4 
for l in lang[::2]:
    print(l)                            # a c
print()

# 5
for l in lang[::-1]:
    print(l)                            # d c b a
print()

# 6
num = [3, -20, -3, 44]
for i in num:
    if i < 0:
        print(i)                        # 음수만 출력
print()

# 7
num = [13, 21, 12, 14, 30, 18]
for i in num:
    if i % 3 == 0 and i < 20:           # 20보다 작은 3의 배수
        print(i)
print()

# 8
a = ['A', 'b', 'c', 'D']
for i in a:
    if i.isupper():                     # 대문자만 출력
        print(i)
print()

# 9
animal = ['dog', 'cat', 'parrot']
for i in animal:
    print(i.capitalize())               # 첫글자 대문자
print()

# 10
file = ['hello.py', 'ex01.py', 'intro.py']
for i in file:
    s = i.split('.')
    print(s[0])                         # py 없애기
print()

# 11
file = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in file:
    s = i.split('.')
    if s[1] == 'h' or s[1] == 'c':
        print(i)                        # .h, .c만 출력하기
print()

# 12
for i in range(3, 31, 3):
    print(i)                            # 3의 배수 출력
print()    

# 13
for i in range(10):
    print(i / 10)
print()

# 14
s = 0
for i in range(1, 11):
    s += i
print(s)                                # 1 ~ 10 합
print()

# 15
s = 0
for i in range(1, 11, 2):               # 홀수 합
    s += i
print(s)
print()

# 16
price = [32100, 32150, 32000, 32500]
for i, data in enumerate(price):
    print(i, data)                      # index, value 출력
print()

# 17
my_list = ['가', '나', '다', '라']
for i in range(len(my_list) - 1):
    print(my_list[i], my_list[i+1])

# 18
my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list) - 2):
    print(my_list[i], my_list[i+1], my_list[i+2])   # 가 나 다, 나 다 라, 다 라 마
print()

# 19
my_list = [100, 200, 400, 800]
for i in range(len(my_list) - 1):
    print(abs(my_list[i] - my_list[i+1]))   # n, n+1 차 출력
print()

# 20
low_price = [100, 200, 400, 800, 1000]
high_price = [150, 300, 430, 880, 1000]
vol = []    # 변동폭
for i in range(len(low_price)):
    vol.append(abs(low_price[i] - high_price[i]))
print(vol)

# 21
apart = [['101호', '102호'], ['201호', '202호'], ['301호', '302호']]
for i in apart:
    for j in i:
        print(j)        # 101 102 201 202 301 302

# 22
stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]

# 23
stock_dict = {'시가': [100, 200, 300], '종가': [80, 210, 330]}
# dict으로 정의

# 24
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart[::-1]:
    for j in i:
        print(j)        # 301 302 201 202 101 102
print()

# 25
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart[::-1]:
    for j in i[::-1]:
        print(j)        # 302 301 202 201 102 101
print()

# 26
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for i in data:
    for j in i:
        print(j * 1.00014)  # 0.0014% 곱한값 출력
        result.append(j * 1.00014)
print(result)       # 1차원 리스트에 저장