# 1
import random


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
class Account:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.bank = 'sc은행'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)           # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3

y = Account('윤서환', 1000)
print(y.name, y.cash, y.bank, y.account_number)       # 윤서환 1000 sc은행 676-95-198616

# 12
class Account:

    account_count = 0

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.bank = 'sc은행'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)           # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
    
    def get_account_num(self):
        print(Account.account_count)

y = Account('안녕', 100)
t = Account('d', 100)
t.get_account_num()