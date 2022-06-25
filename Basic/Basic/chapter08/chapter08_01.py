# Chapter08-01
# 파이썬 내장(Bulit-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 실습

# 절댓값
# abs()

print(abs(-3))

# all, any : iterable 요소 검사(참, 거짓)
print(all([1, 2, 3]))                       # True          -> 0이 하나라도 있으면 False (and)
print(all([1, 2, 0]))                       # False
print(all([1, 2, '']))                      # False

print(any([1, 2, 0]))                       # True          -> 1이 하나라도 있으면 True (or)
print(any([1, 2, 3]))                       # True

# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(67))                              # C
print(ord('C'))                             # 67

# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['a', 'b', 'c']):
    print(i+1, name)                        # 1 a 2 b 3 c

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -5, 2 ,-3, 4])))                # [-5, -3, 4]
print(list(filter(lambda x: abs(x) > 2, [1, -5, 2 ,-3, 4])))    # [-5, -3, 4]

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(int(4)))

# len : 요소의 길이 반환
print(len('abcdefg'))                       # 7
print(len([1,2,3,4,5,6,7]))                 # 7

# max, min : 최댓값, 최솟값
print(max([1,2,3]))                         # 3
print(max('python study'))                  # y
print(min([1,2,3]))                         # 1
print(min('python study'))                  # (공백)

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1, -3, 5, -2, 4, -6])))               # [1, 3, 5, 2, 4, 6]
print(list(map(lambda x: abs(x), [1, -3, 5, -2, 4, -6])))       # [1, 3, 5, 2, 4, 6]

# pow : 제곱값 반환
print(pow(2, 10))                           # 1024

# range : 반복가능한 객체(Iterable) 반환
print(range(1, 10, 2))                      # range(1, 10, 2)
print(list(range(1, 10, 2)))                # [1, 3, 5, 7, 9]
print(list(range(0, -10, -1)))              # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# round : 반올림
print(round(6.5781, 2))                     # 6.58
print(round(5.6))                           # 6

# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6,7,8,9,10]))                    # 40
print(sum(range(1, 101)))                   # 5050

# type : 자료형 확인
print(type(3))                              # <class 'int'>
print(type({}))                             # <class 'dict'>
print(type([]))                             # <class 'list'>
print(type(()))                             # <class 'tuple'>

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10,20,30], [40,50,60])))    # [(10, 40), (20, 50), (30, 60)]
print(list(zip([10,20,30], [40,50])))       # [(10, 40), (20, 50)]  -> 되는 요소까지 튜플화