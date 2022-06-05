# chpater03_05
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용 
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name': 'kim', 'phone': '01033337777', 'birth': '000613'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Yun',
    'City': 'Busan',
    'Age': 23,
    'Grade': 'A',
    'Status': True
}

e = dict([
    ('Name', 'Yun'),
    ('City', 'Busan')
])

f = dict(
    Name='Yun',
    City='Busan',
    Age=23,
    Grade='A',
    Status=True
)

# 출력
print('a : ', a['name'])                # kim
print('a : ', a.get('name'))            # kim

# print('a : ', a['name1'])             # 존재x -> Error
print('a : ', a.get('name1'))           # 존재x -> None
print('b : ', b[0])                     # Hello Python
print('b : ', b.get(0))                 # Hello Python
print('f : ', f.get('City'))            # Busan
print('f : ', f.get('Age'))             # 23

# 딕셔너리 추가 
print(a)                                # {'name': 'kim', 'phone': '01033337777', 'birth': '000613'}
a['address'] = 'Busan'                  
print(a)                                # {'name': 'kim', 'phone': '01033337777', 'birth': '000613', 'address': 'Busan'}
a['rank'] = [1, 2, 3]
print(a)                                # {'name': 'kim', 'phone': '01033337777', 'birth': '000613', 'address': 'Busan', 'rank': [1, 2, 3]}

# 딕셔너리 길이
print('a : ', len(a))                   # 5
print('b : ', len(b))                   # 1
print('c : ', len(c))                   # 1
print('d : ', len(d))                   # 5  -> key개수를 출력함

# 딕셔너리 함수
# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용가능

print('a : ', a.keys())                 # dict_keys(['name', 'phone', 'birth', 'address', 'rank'])
print('b : ', b.keys())                 # dict_keys([0])
print('c : ', c.keys())                 # dict_keys(['arr'])
print('d : ', d.keys())                 # dict_keys(['Name', 'City', 'Age', 'Grade', 'Status'])
print()

print('a : ', a.values())               # dict_values(['kim', '01033337777', '000613', 'Busan', [1, 2, 3]])
print('b : ', b.values())               # dict_values(['Hello Python'])
print('c : ', c.values())               # dict_values([[1, 2, 3, 4]])
print('d : ', d.values())               # dict_values(['Yun', 'Busan', 23, 'A', True])
print('a : ', list(a.values()))         # ['kim', '01033337777', '000613', 'Busan', [1, 2, 3]]
print('a : ', list(b.values()))         # ['Hello Python']
print()

print('a : ', a.items())                # dict_items([('name', 'kim'), ('phone', '01033337777'), ('birth', '000613'), ('address', 'Busan'), ('rank', [1, 2, 3])])
print('b : ', b.items())                # dict_items([(0, 'Hello Python')])
print('c : ', c.items())                # dict_items([('arr', [1, 2, 3, 4])])
print('d : ', d.items())                # dict_items([('Name', 'Yun'), ('City', 'Busan'), ('Age', 23), ('Grade', 'A'), ('Status', True)])
print('a : ', list(a.items()))          # [('name', 'kim'), ('phone', '01033337777'), ('birth', '000613'), ('address', 'Busan'), ('rank', [1, 2, 3])]
print('b : ', list(b.items()))          # [(0, 'Hello Python')]
print()

print(a)                                # {'name': 'kim', 'phone': '01033337777', 'birth': '000613', 'address': 'Busan', 'rank': [1, 2, 3]}
print('a : ', a.pop('name'))            # kim
print('a : ', a)                        # {'phone': '01033337777', 'birth': '000613', 'address': 'Busan', 'rank': [1, 2, 3]}
print()

print('f : ', f)                        # {'Name': 'Yun', 'City': 'Busan', 'Age': 23, 'Grade': 'A', 'Status': True}
print('f : ', f.popitem())              # ('Status', True)
print('f : ', f)                        # {'Name': 'Yun', 'City': 'Busan', 'Age': 23, 'Grade': 'A'}
print('f : ', f.popitem())              # ('Grade', 'A')
print('f : ', f)                        # {'Name': 'Yun', 'City': 'Busan', 'Age': 23}
print('f : ', f.popitem())              # ('Age', 23)
print('f : ', f)                        # {'Name': 'Yun', 'City': 'Busan'}
print('f : ', f.popitem())              # ('City', 'Busan')
print('f : ', f)                        # {'Name': 'Yun'}
print('f : ', f.popitem())              # ('Name', 'Yun')
print('f : ', f)                        # {}   -> 딕셔너리는 시퀀스가 없기 때문에 pop호출 시, random으로 발생
print()

print('a : ', 'birth' in a)             # True
print('a : ', 'birth2' in a)            # False

# 딕셔너리 수정
a['test'] = 'test_dict'
print('a : ', a)                        # {'phone': '01033337777', 'birth': '000613', 'address': 'Busan', 'rank': [1, 2, 3], 'test': 'test_dict'}

a.update(birth='123456')
print('a : ', a)                        # {'phone': '01033337777', 'birth': '123456', 'address': 'Busan', 'rank': [1, 2, 3], 'test': 'test_dict'}

temp = {'address' : 'Seoul'}
a.update(temp)
print('a : ', a)                        # {'phone': '01033337777', 'birth': '123456', 'address': 'Seoul', 'rank': [1, 2, 3], 'test': 'test_dict'}