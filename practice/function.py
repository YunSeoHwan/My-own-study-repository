# 1
from audioop import reverse
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

# 5
def print_reverse(str):
    print(str[::-1])

print_reverse('python')         # nohtyp

# 6
def print_score(list):
    sum = 0
    for i in list:
        sum += i
    print(sum/len(list))
print_score([1, 2, 3])          # 2.0

# 7
def print_even(list):
    for i in list:
        if i % 2 == 0:
            print(i)

print_even([1, 3, 2, 10, 12, 11, 15])   # 2 10 12

# 8
my_dict = {"10/26" : [100, 130, 100, 100], "10/27" : [10, 12, 10, 11]}
def ohlc(dict, key):
    print(dict.get(key))
ohlc(my_dict, '10/26')

# 9
def print_mxn(str, num):
    l = int(len(str) / num)
    for i in range(l+1):
        print(str[i * num : i * num + num])
print_mxn("아이엠어보이유알어걸", 3)

# 10
def calc_monthly_salary(annual_pay):
    monthly_pay = int(annual_pay / 12)
    return monthly_pay
print(calc_monthly_salary(12000000))