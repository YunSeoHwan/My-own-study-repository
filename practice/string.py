# 1
letters = 'python'
print(letters[0:3:2])       # pt  

# 2
license = "24가 2210"
print(license[-4:])         # 2210

# 3
string = "홀짝홀짝홀짝"
print(string[0::2])         # print(string[::2])

# 4
string = 'python'
print(string[::-1])         # nohtyp

# 5
pb = '010-1111-2222'
new_pb = pb.replace("-"," ")
print(new_pb)               # 010 1111 2222

# 6
new_pb2 = pb.replace("-","")
print(new_pb2)              # 01011112222

# 7
url = "http://naver.com"
new_url = url.split('.')
print(new_url)
print(new_url[-1])          # com

# 8
a = 'abcdefghi2a2345dgeg'
new_a = a.replace('a', "A")
print(new_a)                # Abcdefghi2A2345dgeg

# 9
string = 'abcd'
string.replace('b','B')
print(string)               # abcd  -> str은 변경불가 자료형

# 10
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 3)               # python java python java python java

# 11
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print(f'이름 : {name1} 나이 : {age1}')  # 이름 : 김민수 나이 : 10
print(f'이름 : {name2} 나이 : {age2}')  # 이름 : 이철희 나이 : 13
print('이름 : %s 나이 : %s' % (name1, age1))
print('이름 : {0} 나이 : {1}'.format(name2, age2))

# 12
counting = '5,969,782,550'
new_counting = int(counting.replace(',',''))
print(new_counting)                         # 5969782550

# 13
time = '2020/03(E) (IFRS연결)'
print(time[:7])                             # 2020/03

# 14
data = "    삼성전자    "
data1 = data.replace(" ", "")
data2 = data.strip()
print(data1, data2)                         # 삼성전자 삼성전자

# 15
ticker = 'btc_krw'
ticker1 = ticker.upper()
print(ticker1)                              # BTC_KRW

# 16
s = 'hello'
s1 = s.capitalize()
print(s, s1)                                # hello Hello

# 17
file_name = '보고서.xlsx'
check = file_name.endswith('xlsx')
print(check)                                # True

# 18
a = 'hello world'
print(a.split())                            # ['hello', 'world']

# 19
data = "039490      "
print(data.rstrip())                        # 039490