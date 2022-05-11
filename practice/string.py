# 1
letters = 'python'
print(letters[0:3:2])

# 2
license = "24가 2210"
print(license[-4:])

# 3
string = "홀짝홀짝홀짝"
print(string[0::2])     # print(string[::2])

# 4
string = 'python'
print(string[::-1])

# 5
pb = '010-1111-2222'
new_pb = pb.replace("-"," ")
print(new_pb)

# 6
new_pb2 = pb.replace("-","")
print(new_pb2)

# 7
url = "http://naver.com"
new_url = url.split('.')
print(new_url)
print(new_url[-1])

# 8
a = 'abcdefghi2a2345dgeg'
new_a = a.replace('a', "A")
print(new_a)

# 9
string = 'abcd'
string.replace('b','B')
print(string)               # abcd  -> str은 변경불가 자료형