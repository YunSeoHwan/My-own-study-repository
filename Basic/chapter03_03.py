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