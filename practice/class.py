# 1
class Human:
    pass

# 2
areum = Human()

# 3
class Human:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human('서환', 23, '남자')
print('이름 : {}, 나이 : {}, 성별 : {}'.format(areum.name, areum.age, areum.sex))

# 4
class Human:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print('이름 : {}, 나이 : {}, 성별 : {}'.format(self.name, self.age, self.sex))

yun = Human('서환', 23, '남자')
yun.who()

# 5
class Human:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print('이름 : {}, 나이 : {}, 성별 : {}'.format(self.name, self.age, self.sex))
    
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

yun = Human('불명', '미상', '모름')
yun.who()                                   # 이름 : 불명, 나이 : 미상, 성별 : 모름

yun.setInfo('서환', 23, '남자')
yun.who()   # Human.who(yun)                # 이름 : 서환, 나이 : 23, 성별 : 남자

# 6
class Human:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print('나의 죽음을 알리지 마라')

    def who(self):
        print('이름 : {}, 나이 : {}, 성별 : {}'.format(self.name, self.age, self.sex))
    
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
y = Human('서환', 23, '남자')
del y                                       # 나의 죽음을 알리지 마라

# 7
class OMG :
    def print() :
        print("Oh my god")


mystock = OMG()
# mystock.print()      # OMG.print(mystock) --> 에러

# 8
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name
    
a = Stock(None, None)
a.set_name('삼성전자')                       # Stock.set_name(a, '삼성전자')
print(a.name)                               # 삼성전자

# 9
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

a = Stock(None, None)
a.set_code('005930')                        # Stock.set_code(a, 005930)
print(a.code)                               # 005930

# 10
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

s = Stock('삼성전자', '005930')
print(s.name)                               # 삼성전자
print(s.code)                               # 005930
print(s.get_name())                         # 삼성전자
print(s.get_code())                         # 005930

# 11
