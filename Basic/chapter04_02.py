# Chapter04_02
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#     <loop body>

for v1 in range(10):        # 0 ~ 9
    print('v1 : ', v1)

for v2 in range(1, 11):     # 1 ~ 10
    print('v2 : ', v2)

for v3 in range(1, 11, 2):  # 1, 3, 5, 7, 9
    print('v3 : ', v3)

# 1 ~ 1000 합
sum1 = 0

for v in range(1, 1001):
    sum1 += v
print(sum1)                     # 500500

print(sum(range(1, 1001)))      # 500500
print(sum(range(4, 1001, 4)))   # 125500

# 예제1
name = ['kim', 'park', 'yun', 'lee', 'choi']

for names in name:
    print('You are : ', names)  # 순서대로 이름 출력

# 예제2
lotto_num = [11, 12, 15, 19, 21, 44]
for n in lotto_num:
    print(n)

# 예제3
word = 'Beautiful'
for w in word:
    print(w)                    # 한 글자씩 출력

# 예제4
my_info = {
    'name': 'Yun',
    'age': 23,
    'city': 'Busan'
}
for key in my_info:
    print('key : ', my_info.get(key))   # get메소드에 key값에 해당하는 value 리턴

for v in my_info.values():
    print('value : ', v)                # value 리턴

# 예제5
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())                # 대문자만 출력

# Break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
    else:
        print("Not found : ", num)      # 34를 찾으면 for문 탈출

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue                        # 조건 만족시, 다시 반복문으로 올라감
    print("current type : ", type(v))
    print("multiply by 2:", v * 3)

# for - else 구문
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
else:
    print("Not Found 45...")            # break없으면 반복문 끝나고 실행됨

# 구구단 출력
for i in range(2, 10):
    for j in range(2, 10):
        print('{:4d}'.format(i * j), end='')
    print()

# 변환예제
name = 'Aceman'
print('Reversed : ', reversed(name))        # <reversed object at 0x000001D9BECBBFA0> id 값
print('List : ', list(reversed(name)))      # ['n', 'a', 'm', 'e', 'c', 'A']
print('Tuple : ', tuple(reversed(name)))    # ('n', 'a', 'm', 'e', 'c', 'A')
print('Set : ', set(reversed(name)))        # {'A', 'a', 'n', 'e', 'm', 'c'} 순서 x