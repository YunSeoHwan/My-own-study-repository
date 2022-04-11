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