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

# 11