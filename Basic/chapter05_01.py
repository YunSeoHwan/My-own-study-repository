# Chapter05_01
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lambda)

# 함수의 정의 방법
# def function_name(parameter):
    # code

# 예제1
def first_func(w):
    print('Hello,', w)

word = 'Goodboy'
first_func(word)                # Hello, Goodboy

# 예제2
def return_func(w):
    value = "Hello, " + str(w)
    return value

x = return_func('Goodboy2')
print(x)                        # Hello, Goodboy2

# 예제3 (다중반환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
print(x, y, z)                  # 100 200 300

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)         # 튜플로 리턴

q = func_mul2(20)
print(q, type(q))               # (200, 400, 600) <class 'tuple'>

# 리스트 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]         # 리스트로 리턴

l = func_mul3(30)
print(l, type(l))               # [300, 600, 900] <class 'list'>

# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1':y1, 'v2':y2, 'v3':y3}         # 딕셔너리로 리턴

d = func_mul3(40)
print(d, type(d))               # {'v1': 400, 'v2': 800, 'v3': 1200} <class 'dict'>

# 중요
# *args, **kwargs

# *args(언팩킹), 튜플
def args_func(*args):           # 매개변수 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('--------')

args_func('Lee')                            # 0 Lee
args_func('Lee', 'Park')                    # 0 Lee 1 Park
args_func('Lee', 'Park', 'Kim')             # 0 Lee 1 Park 2 Kim

# **kwargs(언팩킹), 딕셔너리
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('--------')

kwargs_func(name1='Lee')                                    # name1 Lee
kwargs_func(name1='Lee', name2='Park')                      # name1 Lee name2 Park
kwargs_func(name1='Lee', name2='Park', name3='Yun')         # name1 Lee name2 Park name3 Yun

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Park', 'Kim', age1=20, age2=30, age3=40)
# 10 20 ('Lee', 'Park', 'Kim') {'age1': 20, 'age2': 30, 'age3': 40}

# 중첩함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In func')
    func_in_func(num + 100)

nested_func(100)                    # In func 200
# func_in_func(1000)                # 호출 불가능