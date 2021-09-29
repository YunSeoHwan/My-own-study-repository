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

   ## 5. 조건문, 반복문
   생략.
   ## 6. 함수
   어떤 일을 수행하는 코드의 묶음.
   ### 6-1 가변인자 사용
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
   ### 6-2 지역변수, 전역변수
   ```python
   gun = 10  # 전역 변수

def check(sol):
  gun = 20  # 지역 변수
  gun = gun - sol
  print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))  # 10
check(2)  # 18
print("전체 총 : {0}".format(gun))  # 10

# 변수에 global을 붙여 전역변수로 사용 가능
```

   ## 7. 입출력
   ### 7-1 표준입출력
   ```python
   import sys
print("Python", "Java", file=sys.stdout)  # 정상처리
print("Python", "Java", file=sys.stderr)  # 에러처리


score = {"수학":100, "영어":80, "과학":20}
for subject, scores in score.items():   # 키 값과 value값을 받음.
  print(subject, scores, sep=" : ")   # sep은 해당 키워드로 분류
# 수학 : 100
# 영어 : 80
# 과학 : 20
  print(subject.ljust(8), str(scores).rjust(4), sep=":")  # 과목은 8칸기준 왼쪽 정렬 
# 수학      : 100
# 영어      :  80
# 과학      :  20

for num in range(1, 21):
  print("대기번호 : " + str(num).zfill(3))    # 0으로 채움
# 대기번호 : 001
# 대기번호 : 002
# ...
```
   ### 7-2 다양한 포멧 출력
   ```python
   # 빈 자리는 빈공간으로 두고 , 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))   # >,< 이 가리키는 방향이 정렬 방향
                                # : 뒤는 채워질 문자, 부등호 뒤 숫자는 공간 확보
#      500

# 양수일 때 +, 음수일 때 - 찍기
print("{0: >+10}".format(500))    #        +500
print("{0: >+10}".format(-500))   #        -500

# 왼쪽 정렬하고, 빈칸으로 _채움
print("{0:_<+10}".format(500))    # +500_____

# 3자리 마다 , 찍어주기
print("{0:+,}".format(100000000)) # 100,000,000

# 소수점 출력
print("{0:f}".format(5/3))  # 1.66667
print("{0:2f}".format(5/3)) # 3째 자리에서 반올림 --> 1.7
```

   ### 7-3 파일 입출력
   ```python
   score_file = open("score.txt", "w", encoding="utf8")  # score.txt 파일을 쓰기(w)
print("수학 : 100", file=score_file)    # score.txt 파일이 생성되고 해당 내용 입력
print("영어 : 80", file=score_file)
score_file.close()    # 항상 close로 마무리

score_file = open("score.txt", "a", encoding="utf8")  # 해당 파일에 덮어쓰기(a)
score_file.write("과학 : 80")   # a는 띄어쓰기 별도로 입력
score_file.write("\n코딩 : 100")
score_file.close()    # score.txt파일에 덮어짐

score_file = open("score.txt", "r", encoding="utf8") # 해당 파일 읽기(r)
print(score_file.read())
score_file.close()
# 수학 : 100
# 영어 : 80
# 과학 : 80
# 코딩 : 100

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")  # 한 줄씩 읽기, 읽고 난 후 커서는 다음 줄 이동
print(score_file.readline(), end="")  
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
# 수학 : 100
# 영어 : 80
# 과학 : 80
# 코딩 : 100

# 파일 전체 읽기
score_file = open("score.txt", "r", encoding="utf8")
while True:
  line = score_file.readline()
  if not line:
    break
  print(line, end="")
score_file.close()
```
   ### 7-4 pickle, with
   ```python
   import pickle
profile_file = open("profile.pickle", "wb")  # pickle 정의. b는 바이너리 약자, 인코딩 안해도 됨.
profile = {"이름":"윤서환", "나이":22}
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
print(profile)
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
```

```python
import pickle
with open("profile.pickle", "rb") as profile_file:  # profile_file 이라는 변수에 저장
  print(pickle.load(profile_file))    # with문 탈출하면서 close 자동 시행

# pickle 없이 파일 읽고 쓰기
with open("test.txt", "w", encoding="utf8") as test_file:
  test_file.write("테스트 파일입니다.")

with open("test.txt", "r", encoding="utf8") as test_file:
  print(test_file.read())   # 테스트 파일입니다.
  ```
   ## 8. 클래스(class)
   쉽게 생각해서 하나의 템플릿이라고 이해하자. ex) 붕어빵 틀
   
   ```python
   class Unit:
  def __init__(self, name, hp, damage):   # init으로 정의
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{0} 유닛이 생성 되었습니다.".format(self.name))
    print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5
# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5
# 탱크 유닛이 생성 되었습니다.
# 체력 150, 공격력 35
```
   ### 8-1 멤버변수
   클래스 내에서 정의된 함수
   ```python
   class Unit:
  def __init__(self, name, hp, damage):   # init으로 정의
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{0} 유닛이 생성 되었습니다.".format(self.name))
    print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 외부에서 객체에 접근

if wraith2 == True:
  print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 레이스 유닛이 생성 되었습니다.
# 체력 80, 공격력 5
# 유닛 이름 : 레이스, 공격력 : 5
# 빼앗은 레이스 유닛이 생성 되었습니다.
# 체력 80, 공격력 5
```
   ### 8-2 메소드
   클래스에 묶여서 관련된 일을 하는 함수
   ```python
   class Unit:
  def __init__(self, name, hp, damage):   # init으로 정의
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{0} 유닛이 생성 되었습니다.".format(self.name))
    print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 공격 유닛
class AttackUnit:
  def __init__(self, name, hp, damage):   # self 는 class안에 있는 자신의 멤버변수 값 사용 안쓰면 전달받은 값 사용
    self.name = name
    self.hp = hp
    self.damage = damage
  
  def attack(self, location):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
    .format(self.name, location, self.damage))

  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
    self.hp -= damage   # 피해받은 만큼 빼기
    print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2회
firebat1.damaged(25)
firebat1.damaged(25)

# 파이어뱃 : 5시 방향으로 적군을 공격합니다. [공격력 16]
# 파이어뱃 : 25 데미지를 입었습니다.
# 파이어뱃 : 현재 체력은 25 입니다.
# 파이어뱃 : 25 데미지를 입었습니다.
# 파이어뱃 : 현재 체력은 0 입니다.
# 파이어뱃 : 파괴되었습니다.
```
   ### 8-3 상속과 다중상속
   클래스에서 클래스의 내용(속성과 메소드)를 물려받는 것.
```python
    # 일반 유닛
class Unit:
  def __init__(self, name, hp): 
    self.name = name
    self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # Unit 상속
  def __init__(self, name, hp, damage):
    Unit.__init__(self, name, hp) # Unit으로 상속받은 name, hp
    self.name = name
    self.hp = hp
    self.damage = damage

# 날 수 있는 기능 가진 클래스
class Flyable:
  def __init__(self, fly_speed):
    self.fly_speed = fly_speed
  
  def fly(self, name, location):
    print("{0} : {1} 시 방향으로 날아갑니다. [속도 {2}]"\
    .format(name, location, self.fly_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):   # 다중 상속
  def __init__(self, name, hp, damage, fly_speed):  # 정의
    AttackUnit.__init__(self, name, hp, damage)
    Flyable.__init__(self, fly_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 발키리 : 3시 시 방향으로 날아갑니다. [속도 5]
```
   ### 8-4 메소드 오버라이딩
   자식 클래스가 부모 클래스의 메소드를 특정 형태로 변형해서 구현하는 것
   ```python
   # 일반 유닛
class Unit:
  def __init__(self, name, hp): 
    self.name = name
    self.hp = hp
  
  def move(self, location):
    print("지상 유닛 이동")
    print("{0} : {1} 시 방향으로 이동합니다. [속도 {2}]"\
    .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # Unit 상속
  def __init__(self, name, hp, damage):
    Unit.__init__(self, name, hp) # Unit으로 상속받은 name, hp
    self.name = name
    self.hp = hp
    self.damage = damage

# 날 수 있는 기능 가진 클래스
class Flyable:
  def __init__(self, fly_speed):
    self.fly_speed = fly_speed
  
  def fly(self, name, location):
    print("{0} : {1} 시 방향으로 날아갑니다. [속도 {2}]"\
    .format(name, location, self.fly_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):   # 다중 상속
  def __init__(self, name, hp, damage, fly_speed):  # 정의
    AttackUnit.__init__(self, name, hp, damage)
    Flyable.__init__(self, fly_speed)
  
  def move(self, location):
    print("[공중 유닛 이동]")
    self.fly(self.name, location)   # 메소드 오버라이딩

vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("3시")

# 지상 유닛 이동
# 벌쳐 : 11시 시 방향으로 이동합니다. [속도 10]
# [공중 유닛 이동]
# 배틀크루저 : 3시 시 방향으로 날아갑니다. [속도 3]
```
