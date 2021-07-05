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
# 머신러닝   
