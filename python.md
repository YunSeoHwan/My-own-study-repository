python web scrapping
====================
### 스크래퍼
1. BeautifulSoup   
HTML 및 XML 파일에서 데이터를 가져 오기위한 Python 라이브러리다.
실제 작업을 위해서는 Requests와 함께 사용된다.
2. Requests   
Requests 는 Apache License 2.0에 따라 릴리스 된 Python HTTP 라이브러리다. 
이 프로젝트의 목표는 HTTP 요청을보다 간단하고 인간 친화적으로 만드는 것이다. - 나무위키

### 이론 및 문법
1. 자료형   
숫자, 문자열, bool 자료형 모두가 가능함. 변수를 통해 처리가 가능하다.   
주석의 경우 `#`으로 처리가능하며, 일괄로 주석처리를 하기 위해서는 대상을 drag후, `ctrl + /`를 눌러주면 된다.
2. 연산자   
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
