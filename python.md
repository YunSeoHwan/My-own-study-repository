python web scrapping
====================
### 스크래퍼
1. BeautifulSoup   
HTML 및 XML 파일에서 데이터를 가져 오기위한 Python 라이브러리다.
실제 작업을 위해서는 Requests와 함께 사용된다.
2. Requests   
Requests 는 Apache License 2.0에 따라 릴리스 된 Python HTTP 라이브러리다. 
이 프로젝트의 목표는 HTTP 요청을보다 간단하고 인간 친화적으로 만드는 것이다. - 나무위키

# 이론 및 문법
## 1. 자료형   
숫자, 문자열, bool 자료형 모두가 가능함. 변수를 통해 처리가 가능하다.   
주석의 경우 `#`으로 처리가능하며, 일괄로 주석처리를 하기 위해서는 대상을 drag후, `ctrl + /`를 눌러주면 된다.
## 2. 연산자   
기본적인 사칙연산과 거듭제곱, 몫, 나머지 연산도 가능.   
추가적으로 논리값을 통한 연산도 가능하다. ※참고 `and = &`, `or = |`   
```python   
num = 2
print(num + 2) # 4
num +=2 # num = num + 2
print(num) # 6
```
```python
print(abs(-5)) # 5 절댓값
print(pow(4,2)) # 16 제곱근
print(max(5,10)) # 10 최댓값
print(min(5,10)) # 5 최솟값
print(round(3.14)) # 3 반올림
print(round(4.9)) # 5 
```
## 3. 문자열 처리   
슬라이싱이나 문자열 처리함수를 통해서 활용이 가능하다.   

   ### 3-1 슬라이싱   
```python
number = "001023-1234567"

print("성별 : " + number[7])
print("연 : " + number[0:2]) # 0 부터 2 직전까지
print("월 : " + number[2:4])
print("일 : " + number[4:6])

print("생년월일 : " + number[:6]) # 처음부터 6 직전까지 
print("뒤 7자리 : " + number[7:]) # 7 부터 끝까지
print("뒤 7자리(뒤부터) : " + number[-7:]) # 맨 뒤에서부터 7번째 끝까지
```
   ### 3-2 문자열 처리함수   
   ```python
   python = "Python is Beautiful"

print(python.lower()) # 소문자로 출력 -> python is beautiful
print(python.upper()) # 대문자로 출력 -> PYTHON IS BEAUTIFUL
print(python[0].isupper()) # 첫 문자열이 대문자인지 -> True

print(len(python)) # 문자열 길이 -> 19
print(python.replace("Python", "Java")) # 문자열 교체 -> Java is Beautiful

index = python.index("t") # t이 몇번째에 있는지 -> 2
print(index)

index = python.index("t",index + 1) # 그 다음 t는 언제 나오는지 -> 14
print(index)

print(python.find("t")) # index와 값을 찾아주지만 값이 없을 시, -1 return
```
## 4. 자료구조   
다양한 자료구조들이 있지만, 가장 많이 사용되는 리스트(list), 딕셔너리(dictionary), 튜플(tuple)에 대해 다룸.   

   ### 4-1 리스트(list)
   ```python
   jobs = ["개발자", "교사", "경찰"] # 리스트 정의
print(jobs) # ['개발자', '교사', '경찰']

print(jobs.index("교사")) # object를 넣으면 위치를 알려줌. -> 1

jobs.append("의사") # list에 값을 추가함.
print(jobs) # ['개발자', '교사', '경찰','의사']  

jobs.insert(1,"야구선수") # 해당 위치에 object를 할당.
print(jobs) # ['개발자', '야구선수' ,'교사', '경찰','의사']  

num_list = [2,4,3,7,5]

num_list.sort() # list 순서 정렬
print(num_list) # [2, 3, 4, 5, 7]

num_list.reverse() # list 역순 정렬
print(num_list) #[7, 5, 4, 3, 2]
```

   ### 4-2 딕셔너리(dictionary)
   하나의 키 값에 하나의 value 값이 존재함.
   ```python
   dic = {1:"apple", 100:"banana"}

print(dic[1])   # 해당 키에 맞는 value값이 출력됨.
print(dic[100])

print(dic.get(1))   # 해당 키에 value값을 찾아줌.
#print(dic[2])     # 해당 키 값이 없으면 Error
print(dic.get(2))   # get 사용시 값이 없어도 Error 안뜨고 none 출력
print(dic.get(2, "사용 가능")) # none 대신 다른 문구 사용시

print(1 in dic)  # True
print(2 in dic)  # False

dic = {"A-1":"apple", "B-1":"banana"}

dic["A-1"] = "lemon"  # 기존 value값을 바꿈.
dic["C-1"] = "peach"  # value 추가

print(dic)    # {'A-1': 'lemon', 'B-1': 'banana', 'C-1': 'peach'}

del dic["A-1"]  # 지정한 키에 해당하는 value값 제거

print(dic.keys())   # 키 값만 출력
print(dic.values()) # value 값만 출력

print(dic.items())  # 키, value 값 모두 출력
print(dic.clear())  # 딕셔너리 제거
```

   ### 4-3 튜플(tuple)
   값을 변경할 수 없음.
   ```python
   menu = ("김밥", "라면")   # 튜플 지정 방식
print(menu[0])
print(menu[1])

menu.add("떡볶이")    # Error 값 추가 안됨.

(name, age, hobby) = ("서환", 21, "코딩")   # 한 번에 튜플 지정
```

   ### 4-4 세트(set)
   중복된 값을 제거.
   ```python
   num_set = {1,2,3,3,3}   # set 지정

print(num_set)  # {1, 2, 3}

java = {"유재석" ,"조세호", "박명수"}   
python = set(["유재석" ,"윤서환"])    # set의 또 다른 지정법

# 교집합
print(java & python)    # {'유재석'}
print(java.intersection(python))

# 합집합
print(java | python)    # {'유재석', '조세호', '박명수', '윤서환'}
print(java.union(python))

# 차집합
print(java - python)    # {'조세호', '박명수'}
print(java.difference(python))

# 값 추가, 제거
java.add("김종국")    # 값 추가
python.remove("유재석")   # 값 제거
```

   ### 5. 조건문, 반복문
   생략.
   ### 6. 함수
   어떤 일을 수행하는 코드의 묶음.
   ### 6.1 가변인자 사용
   ``` python
   def profile1(name, age, lan1, lan2, lan3):
  print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # 엔터가 아닌 공백으로 끝냄
  print(lan1, lan2, lan3)   # 뒤에 출력

profile1("윤서환", 22, "python", "java", "c")   # 함수 호출
# 문제점 : 변수에 해당하는 value가 많거나 혹은 적을 경우 수정 불가피


# 해결책
def profile2(name, age, *lan):    # 가변인자 사용
  print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # 엔터가 아닌 공백으로 끝냄
  for l in lan:   # 반복문으로 출력
    print(l, end=" ")   # 공백으로 구분
  print()

profile2("윤서환", 22, "python", "java", "c")
profile2("유재석", 26, "python", "java", "c", "c++")
```
# 머신러닝   
