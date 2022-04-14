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