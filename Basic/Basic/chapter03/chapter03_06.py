#Chapter03_06
# 집합(set)의 특징
# 집합(set) 자료형(순서x, 중복x)

# 선언

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'quz', 'foo', 'baz'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a : ', type(a), a)               # <class 'set'> set()
print('b : ', type(b), b)               # <class 'set'> {1, 2, 3, 4}
print('c : ', type(c), c)               # <class 'set'> {1, 4, 5, 6}
print('d : ', type(d), d)               # <class 'set'> {1, 2, 'Pen', 'Plate', 'Cap'}
print('e : ', type(e), e)               # <class 'set'> {'quz', 'foo', 'bar', 'baz'}
print('f : ', type(f), f)               # <class 'set'> {42, 3.14159, 'foo', (1, 2, 3)}

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t : ', type(t), t)               # <class 'tuple'> (1, 2, 3, 4)
print('t : ', t[1:3])                   # (2, 3)  -> tuple은 시퀀스가 있기 때문에 슬라이싱 가능
print()

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)
print(l)                                # [1, 4, 5, 6]
print(l2)                               # ['foo', 'quz', 'bar', 'baz']

# 길이
print(len(a))                           # 0
print(len(b))                           # 4
print(len(c))                           # 4
print(len(d))                           # 5
print(len(e))                           # 4
print(len(f))                           # 4

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2)                # s1 & s2 :  {4, 5, 6}
print('s1 & s2 : ', s1.intersection(s2))    # s1 & s2 :  {4, 5, 6}  -> get함수와 같이 값이 없으면 None반환

print('s1 | s2 : ', s1 | s2)                # s1 | s2 :  {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('s1 | s2 : ', s1.union(s2))           # s1 | s2 :  {1, 2, 3, 4, 5, 6, 7, 8, 9}  -> get함수와 같이 값이 없으면 None반환

print('s1 - s2 : ', s1 - s2)                # s1 - s2 :  {1, 2, 3}
print('s1 - s2 : ', s1.difference(s2))      # s1 - s2 :  {1, 2, 3}  -> get함수와 같이 값이 없으면 None반환

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2))      # False -> 중복이 존재하면 False, 그렇지 않으면 True 반환

# 부분 집합 확인
print(s1.issubset(s2))                      # False
print(s1.issuperset(s2))                    # False     부분집합 반대개념 s2가 s1을 포함하는지

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print(s1)                                   # {1, 2, 3, 4, 5}

s1.remove(2)
print(s1)                                   # {1, 3, 4, 5}
s1.discard(1)
print(s1)                                   # {3, 4, 5}   -> -> get함수와 같이 값이 없으면 None반환