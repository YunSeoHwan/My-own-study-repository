# Chapter04_03
# 파이썬 반복문
# While 실습

# while <expr>:
#   <statement(s)>

# 예제 1

n = 5
while n > 0:
    print(n)
    n = n - 1                       # 5 4 3 2 1 

# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())                  # baz bar foo

# if 중첩
# 예제3
# break , continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')                # 4 3 Loop Ended.
print()

# 예제4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')                # 4 3 1 0 Loop Ended.

# 예제5
i = 1

while i <= 10:
    print('i :',i)                  # 1 2 3 4 5 6
    if i == 6:
        break
    i += 1

# While - else 구문

# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)                        # 9 8 7 6 5
    if n == 5:
        break
else:
    print('else out.')              # break 없이 반복문 종료시, 출력

# 예제7 
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        break                       # baz bar foo
    i += 1
else:
    print(s, 'not found in list.')

# 무한반복
# while True:
#     print('Foo')

# 예제8
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())
