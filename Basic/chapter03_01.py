# chapter03_01
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Java'
float = 10.0
int = 7
list = [str1, str2]
dict = {
    "name" : "Machine Learning",
    "version" : 2
}
tuple = (7, 8, 9)       # ()없이 ,로 선언 가능
tuple2 = 1, 2, 3
set = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))           # str
print(type(bool))           # bool
print(type(str2))           # str
print(type(float))          # float
print(type(int))            # int
print(type(list))           # list
print(type(dict))           # dict
print(type(tuple))          # tuple
print(type(tuple2))         # tuple
print(type(set))            # set

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) == x**y -> x의 y제곱 
"""

# 정수 선언
i = 77
i2 = -14
big_int = 7777777777777777777777777777888888888888888888888

print(i)                # 77
print(i2)               # -14
print(big_int)          # 7777777777777777777777777777888888888888888888888

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939

# +
print(">>>>> + ")
print("i1 + i2 : ", i1 + i2) 
print("f1 + f2 : ", f1 + f2) 
print("big_int1 + big_int2 : ", big_int1 + big_int2) 

# -
print(">>>>> -")
print("i1 - i2: ", i1 - i2) 
print("f1 - f2: ", f1 - f2)
print("big_int1 - big_int2: ", big_int1 - big_int2)

# *
print(">>>>> *")
print("i1 * i2: ", i1 * i2)
print("f1 * f2: ", f1 * f2)
print("big_int1 * big_int2: ", big_int1 * big_int2)

# /
print(">>>>> /")
print("i2 / i1: ", i2 / i1)
print("f2 / f1: ", f2 / f1)
print("big_int2 / big_int1: ", big_int2 / big_int1)

# //
print(">>>>> //")
print("i2 // i1: ", i2 // i1) 
print("f2 // f1: ", f2 // f1)
print("big_int2 // big_int1: ", big_int2 // big_int1)

# %
print(">>>>> %")
print("i1 % i2 :", i1 % i2)
print("f1 % f2 :", f1 % f2)
print("big_int1 % big_int2 :", big_int1 % big_int2)

# **
print(">>>>> **")
print("2 ** 3: ", 2 ** 3)
print("i1 ** i2: ", i1 ** i2) 
print("f1 ** f2: ", f1 ** f2)