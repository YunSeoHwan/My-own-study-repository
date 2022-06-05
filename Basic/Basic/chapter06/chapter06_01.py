# Chapter06_1
# 파이썬 클래스
# OOP (객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog:  # object 상속
    # 클래스 속성
    species = 'firstdog'            # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog('mikky', 2)
b = Dog('baby', 3)
# c = Dog('mikky', 2)               # a와 다른 객체

# 비교
print(a == b, id(a), id(b))         # False

# 네임스페이스
print('dog1', a.__dict__)           # dog1 {'name': 'mikky', 'age': 2}
print('dog2', b.__dict__)           # dog2 {'name': 'baby', 'age': 3}

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))     # mikky is 2 and baby is 3

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))                 # mikky is a firstdog

print(Dog.species)                  # firstdog
print(a.species)                    # firstdog
print(b.species)                    # firstdog

# 예제2
# self의 이해
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))             # 2827119491920
        print('Func2 called')

f = SelfTest()

print(id(f))                        # 2827119491920
# f.func1()                         # 예외
f.func2()                           # Func2 called

SelfTest.func1()                    # Func1 called
# SelfTest.func2()                  # 예외
SelfTest.func2(f)                   # Func2 called 2827119491920

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0                   # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Yun')

print(Warehouse.stock_num)          # 2

print(user1.name)                   # Lee
print(user2.name)                   # Yun
print(user1.__dict__)               # {'name': 'Lee'}
print(user2.__dict__)               # {'name': 'Yun'}
print(Warehouse.__dict__)           # stock_num': 2 ...
print(user1.stock_num)              # 2

del user1
print(Warehouse.stock_num)          # 1