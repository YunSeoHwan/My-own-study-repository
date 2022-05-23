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
