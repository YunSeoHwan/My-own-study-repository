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