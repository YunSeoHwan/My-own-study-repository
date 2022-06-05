# Chapter05_02
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str)

# 예제1
name = input('Enter your name : ')
grade = input('Enter your grade : ')
company = input('Enter your company name : ')

print(name, grade, company)

# 예제2
number = input('Enter number : ')
name = input('Enter your name : ')

print('type of number', type(number))
print('type of name', type(name))           # 기본형은 반드시 str 나옴

# 예제3
first_number = int(input('Enter number1 : '))
second_number = int(input('Enter number2 : '))

total = first_number + second_number
print('first number + second number : ', total)

# 예제4
float_number = float(input('Enter a float number : '))
print('input float : ', float_number)
print('input type : ', type(float_number))

# 예제5
print('FirstName : {0}, LastName : {1}'.format(input('Enter first name : '), input('Enter second name : ')))