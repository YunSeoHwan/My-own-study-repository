# chapter02_02
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)                # 700
print(type(n))          # int

# 동시 선언
x = y = z = 700
print(x, y, z)          # 700 700 700

# 재선언
var = 700
var = 'change'

print(var)              # change
print(type(var))        # str

# Object References
# 변수 값 할당 상태

# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# ex1)
print(300)
print(int(300))

# ex2)
# n -> 777
n = 777

print(n, type(n))       # 777 int

m = n
# m -> 777 <- n
print(m, n)             # 777 777
print(type(m), type(n)) # int int

m = 400
print(m, n)             # 400 777
print(type(m), type(n)) # int int

# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 500

print(id(m))            # 2647217331280(주소값)
print(id(n))            # 2647217331376
print(id(n) == id(m))   # false

# 같은 오브젝트 참조
m = 800
n = 800

print(id(n))            # 2931810229328
print(id(m))            # 2931810229328
print(id(n) == id(m))   # true
# 값이 동일하다면 하나의 오브젝트로 생성 -> python 내부에서 변수 하나만 할당

# 다양한 변수 선언
# Camel Case : numberOfCollege  -> Method
# Pascal Case : NumberOfCollege -> Class
# Snake Case : number_of_college

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명 불가능()
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""