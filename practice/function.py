# 1
from re import M


def print_hello():
    print('Hello!')
print_hello()                   # Hello!
print()

# 2
def smile(str):
    print(str + ':D')
smile('hi')                     # hi:D
print()

# 3
def calc(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
calc(3, 4)                      # 7 -1 12 0.75
print()

# 4
def max_num(a, b, c):
    m = 0
    if a > m:
        m = a
    if b > m:
        m = b
    if c > m:
        m = c
    print(m)
max_num(0, 1, 2)                # 2