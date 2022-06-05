# chapter02_01
# print 사용법

# 기본 출력
print('Python Start!')          # Python Start!
print("Python Start!")          # Python Start!
print('''Python Start!''')      # Python Start!
print("""Python Start!""")      # Python Start!

print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')     # PYTHON
print('010', '1234', '5678', sep='-')           # 010-1234-5678
print('dbstjghks', 'naver.com', sep='@')        # dbstjghks@naver.com

print()

# end 옵션
print('Welcome to', end=' ')        # Welcome to Python World
print('Python', end = ' ')          # 줄바꿈 사라짐
print('World')

print()

# file 옵션
import sys

print('Learn Python', file=sys.stdout)      # Learn Python(파일 입출력에서 자세하게 다룸)
print()

# format 사용 (d : 정수, s : 문자열, f : 실수)
print('%s %s' % ('one', 'two'))             # one two
print('{} {}'.format('one', 'two'))         # one two
print('{1} {0}'.format('one', 'two'))       # two one

print()

# %s (공백은 *로 표시함)
print('%10s' % ('Hello'))               # *****Hello           
print('{:>10}'.format('Hello'))         # *****Hello

print('%-10s' % ('Hello'))              # Hello*****             
print('{:10}'.format('Hello'))          # Hello*****

print('{:$>10}'.format('Hello'))        # $$$$$Hello
print('{:<10}'.format('Hello'))         # Hello*****
print('{:^10}'.format('Hello'))         # **Hello*** (가운데 정렬)

print('%.5s' % ('python'))              # pytho
print('{:10.5}'.format('pythonstudy'))  # pytho*****

# %d
print('%d %d' % (1,2))                  # 1 2
print('{} {}'.format(1,2))              # 1 2

print('%4d' %(42))                      # **42
print('%4d' %(12345))                   # 12345 (할당 숫자보다 클 경우 다 출력)
print('{:4d}'.format(42))               # **42 (반드시 d 입력)

print('{:^10d}'.format(12345))          # **12345***

print()

# %f
print('%f' %(3.141595364))              # 3.141595
print('{:f}'.format(3.141595364))       # 3.141595 (일반적으로 6자리까지 출력)

print('%1.9f' %(3.141595364))           # 3.141595364
print('%1.15f' %(3.141595364))          # 3.141595364000000 (부동소수점 붙음)

print('%06.2f' %(3.1415936489))         # 003.14 (6자리 중 정수부분 빈자리는 0으로 채우고 나머지 소수부분 출력)
print('{:06.2f}'.format(3.1415936489))  # 003.14
print('%04.6f' %(3.1415936489))         # 3.141594 (소수부분이 정수부분보다 더 작아야함.)
