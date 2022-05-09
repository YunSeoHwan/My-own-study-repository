# chapter03_02
# 파이썬 문자형

# 문자열 생성
from soupsieve import escape


str1 = 'Hello Python'
str2 = "Who am i?"
str3 = """Python"""
str4 = '''Thank you!'''

print(len(str1), len(str2), len(str3), len(str4))   # 12 9 6 10 -> 공백 포함 문자열 길이

# 빈 문자열
empty_str1 = ''
empty_str2 = str()

print(type(empty_str1), len(empty_str1))            # str 0
print(type(empty_str2), len(empty_str2))            # str 0

# 이스케이프 문자 사용

"""
참고 : Escape 코드

\n : 줄바꿈
\t : 탭
\\ : \
\' : '
\" : "
\000 : 널 문자
...

"""

print("I'm a boy")              # I'm a boy
print('I\'m a boy')             # I'm a boy
print("I\\m a boy")             # I\m a boy
print("a\tb")                   # a       b
print("a \"\" b")               # a "" b

escape_str1 = "Do you have a \"retro game\"?"
escape_str2 = 'What\'s on TV?'

print(escape_str1)              # Do you have a "retro game"?
print(escape_str2)              # What's on TV?

# 탭, 줄바꿈
t_s1 = "Click\tStart!"
t_s2 = "Now Line\nCheck!"

print(t_s1)                     # Click   Start!
print(t_s2)                     # Now Line
                                # Check!

# Raw String
raw_s = r'D:\python\test'
print(raw_s)                    # D:\python\test

# 멀티라인 입력
multi_str = \
'''
문자열
멀티라인 입력
테스트
'''
print(multi_str)            # 문자열
                            # 멀티라인 입력
                            # 테스트

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you?"
str_o4 = "Busan Seoul Daejeon"

print(str_o1 * 3)           # PythonPythonPython
print(str_o1 + str_o2)      # PythonApple
print('p' in str_o1)        # True
print('y' in str_o2)        # False
print('P' in str_o2)        # False
print('P' not in str_o2)    # True

# 문자열 형 변환
print(str(66), type(str(66)))           # 66 str
print(str(True), type(str(True)))       # True str 
print(str(10.1), type(str(10.1)))       # 10.1 str

# 문자열 함수 (upper, isalnum, count, isalpha...)
print("Capitalize : ", str_o1.capitalize())         # Capitalize :  Python  -> 첫 글자 대문자
print("endswith : ", str_o2.endswith("!"))          # endswith :  False  -> 마지막 글자 확인 ex) 마침표 여부 확인
print("replace : ", str_o1.replace("thon", "Good")) # replace :  pyGood
print("sorted : ", sorted(str_o1))                  # sorted :  ['h', 'n', 'o', 'p', 't', 'y']
print("split : ", str_o4.split(" "))                # split :  ['Busan', 'Seoul', 'Daejeon']

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str))      # __iter__ 가 존재하면 시퀀스

# 출력