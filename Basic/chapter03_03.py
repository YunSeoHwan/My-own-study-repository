# chapter 03_3
# Python List
# 자료구조에서 중요
# 리스트 자료형 (순서 o, 중복 o, 수정 o, 삭제 o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'food', 3, 4, False, 3.14159]

# 인덱싱
print('d : ', type(d), d)                   # <class 'list'> [1000, 10000, 'Ace', 'Base', 'Captine']
print('d : ', d[1])                         # 10000
print('d : ', d[0] + d[1] + d[1])           # 21000
print('d : ', d[-1])                        # Captine
print('e : ', e[-1][1])                     # Base      -> [배열인덱싱][인덱싱한 배열의 인덱스]
print('e : ', list(e[-1][1]))               # ['B', 'a', 's', 'e']

# 슬라이싱
print('d : ', d[0:3])                       # [1000, 10000, 'Ace']
print('d : ', d[2:])                        # ['Ace', 'Base', 'Captine']
print('d : ', e[-1][1:3])                   # ['Base', 'Captine']
print('d : ', e[-1][1:6])                   # ['Base', 'Captine']   -> 리스트 길이보다 길면, 존재하는 인덱스까지 출력

# 연산
print('c + d : ', c + d)                    # [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Captine']
print('c * 3 : ', c * 3)                    # [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
print("'Test' + c[0]", 'Test' + str(c[0]))  # Test70

# 값비교
print(c == c[:3] + c[3:])                   # True
print(c)                                    # [70, 75, 80, 85]
print(c[:3] + c[3:])                        # [70, 75, 80, 85]

# Identify(id)
temp = c
print(temp, c)                              # 같은 id값을 가짐
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
c[0] = 4
print('c : ', c)                            # [4, 75, 80, 85]

c[1:2] = ['a', 'b', 'c']                    
print('c : ', c)                            # [4, 'a', 'b', 'c', 80, 85]

c[1:2] = [['a', 'b', 'c']]
print('c : ', c)                            # [4, ['a', 'b', 'c'], 'b', 'c', 80, 85]

c[1] = ['a', 'b', 'c']
print('c : ', c)                            # [4, ['a', 'b', 'c'], 'b', 'c', 80, 85]

c[1:3] = []                                 
print('c : ', c)                            # [4, 'c', 80, 85]

del c[2]
print('c : ', c)                            # [4, 'c', 85]

# 리스트 함수
a = [5, 4 ,2 ,1, 3]

a.append(10)
print('a : ', a)                            # [5, 4, 2, 1, 3, 10]

a.sort()
print('a : ', a)                            # [1, 2, 3, 4, 5, 10]

a.reverse()
print('a : ', a)                            # [10, 5, 4, 3, 2, 1]
print('a : ', a.index(3), a[3])             # 3 3  -> index값 호출하는 방법
a.reverse()

a.insert(2,7)   
print('a : ', a)                            # [1, 2, 7, 3, 4, 5, 10]

a.remove(10)
print('a : ', a)                            # [1, 2, 7, 3, 4, 5]

print('a : ', a.pop())                      # 5
print('a : ', a)                            # [1, 2, 7, 3, 4]     -> last index값 불러오고 remove

print('a : ', a.count(4))                   # 1  -> value 수 return

ex = [8, 9]
a.extend(ex)
print('a : ', a)                            # [1, 2, 7, 3, 4, 8, 9]

# 반복문 활용
while a:
    data = a.pop()
    print(data)