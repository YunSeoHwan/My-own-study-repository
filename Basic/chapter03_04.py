# chapter03_04
# python tuple
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x)   # 불변

# 선언
a = ()   
b1 = (1)
b2 = (1,)
print(type(b1), type(b2))                   # <class 'int'> <class 'tuple'>

c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('d : ', d[1])                         # 1000
print('d : ', d[0] + d[1] + d[1])           # 2100
print('d : ', d[-1])                        # Captine
print('e : ', e[-1])                        # ('Ace', 'Base', 'Captine')
print('e : ', e[-1][1])                     # Base        
print('e : ', list(e[-1][1]))               # ['B', 'a', 's', 'e']

# 수정x
# d[0] = 1500                               # error

# 슬라이싱
print('d : ', d[0:3])                       # (100, 1000, 'Ace')
print('d : ', d[2:])                        # ('Ace', 'Base', 'Captine')
print('e : ', e[2][1:3])                    # ('Base', 'Captine')

# 튜플 연산
print('c + d : ', c + d)                    # (11, 12, 13, 14, 100, 1000, 'Ace', 'Base', 'Captine')
print('c * 3 : ', c * 3)                    # (11, 12, 13, 14, 11, 12, 13, 14, 11, 12, 13, 14)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a : ', a)                            # (5, 2, 3, 1, 4)
print('a : ', a.index(3))                   # 2

# 팩킹 & 언팩킹

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')
print(t)                                    # ('foo', 'bar', 'baz', 'qux')
print(t[0])                                 # foo
print(t[-1])                                # qux

# 언팩킹
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))   # str str str str
print(x1, x2, x3, x4)                           # foo bar baz qux

# 팩킹 & 언팩킹
t2 = 1, 2, 3                            # ()생략 가능 -> tuple
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)                               # (1, 2, 3)
print(t3)                               # (4,)
print(x1, x2, x3)                       # 1 2 3
print(x4, x5, x6)                       # 4 5 6