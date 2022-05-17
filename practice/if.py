# 1
print((3 == 3) and (4 != 3))        # True

# 2
user = input()
if user == '안녕하세요':
    print('안녕하세요' * 2)

# 3
user = int(input())
print(user + 10)

# 4
num = int(input())
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 5
num = int(input())
if num + 20 < 255:
    print(num + 20)
else:
    print(255)

# 6
time = input('현재시간: ')
if time[-2:] == '00':
    print('정각입니다.')
else:
    print('정각이 아닙니다.')

# 7
fruit = ['사과', '포도', '홍시']
user = input('좋아하는 과일은?')
if user in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')

# 8
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input('좋아하는 계절은 : ')
if user in fruit:
    print('정답입니다')
else:
    print('오답입니다.')

# 9
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input('좋아하는 계절은 : ')
if user in fruit.values():
    print('정답입니다.')
else:
    print('오답입니다.')

# 10
user = input()
if user.islower():
    print(user.upper())
else:
    user.lower()

# 11
transfer = {'달러': 1167, '엔': 1.096, '유로': 1268, '위안': 171}
user = input()
a, b = user.split()
print(float(a) * transfer[b])

# 12
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n1 and n2 >= n3:
    print(n2)
else:
    print(n3)

# 13
phone = {'011': 'SKT', '016': 'KT', '019': 'LGU', '010': '알수없음'}
user = input('전화번호')
print(phone[user[:3]])

# 14
id = input('주민번호 : ')
if id[7] == '1' or id[7] == '3':
    print('남자')
else:
    print('여자')