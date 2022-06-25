# Chapter08_02
# 파이썬 외장(External) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예제1
import sys
from weakref import WeakValueDictionary
print(sys.argv)

# 예제2(강제종료)
# sys.exit()

# 예제3(파이썬 패키지 위치)
print(sys.path)

# pickle : 객체 파일 읽기, 쓰기
import pickle

# 예제4(쓰기)
f = open('test.obj', 'wb')
obj = {1: 'python', 2: 'study', 3:'basic'}
pickle.dump(obj, f)
f.close()

# 예제5(읽기)
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))                 # {1: 'python', 2: 'study', 3: 'basic'} <class 'dict'>
f.close()

# os : 환경 변수, 디렉터리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), rename

# 예제6
import os
print(os.environ)
print(os.environ['USERNAME'])           # yun123

# 예제7
print(os.getcwd())                      # C:\python_study

# time : 시간 관련 처리
import time

# 예제8
print(time.time())                      # 1656163492.6547303

# 예제9(형태 변환)
print(time.localtime(time.time()))      # time.struct_time(tm_year=2022, tm_mon=6, tm_mday=25, tm_hour=22, tm_min=34, tm_sec=46, tm_wday=5, tm_yday=176, tm_isdst=0)

# 예제10(간단 표현)
print(time.ctime())                     # Sat Jun 25 22:35:30 2022

# 예제11(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))      # 2022-06-25 22:36:53

# 예제12(시간 간격 발생)
for i in range(6):
    print(i)
    time.sleep(1)                       # 1초마다 실행

# random : 난수 리턴
import random

# 예제13
print(random.random())                  # 0 ~ 1 실수

# 예제14
print(random.randint(1,45))             # 1 ~ 45
print(random.randrange(1,45))           # 1 ~ 44

# 예제15(섞기)
d = [1,2,3,4,5]
random.shuffle(d)
print(d)                                # [3, 2, 4, 5, 1]

# 예제16(무작위 선택)
c = random.choice(d)
print(d)

# webbrowser : 본인 os의 웹 브라우저 실행
import webbrowser

webbrowser.open('http://naver.com')

webbrowser.open_new('http://naver.com')