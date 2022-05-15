# 1
temp = dict()
print(temp)

# 2
ice_cream = dict(
    메로나=1000,
    폴라포=1200,
    빵빠레=1800
)

ice_cream2 = {
    '메로나': 1000,
    '폴라포': 1200,
    '빵빠레': 1800
}
print(ice_cream)                # {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
print(ice_cream2)               # {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}

# 3
ice_cream.update(죠스바=1200)
ice_cream.update(월드콘=1500)
print(ice_cream)                # {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}

new_ice = {'죠스바': 1200, '월드콘': 1500}
ice_cream2.update(new_ice)
print(ice_cream2)               # {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}

# 4
print('메로나 가격 : ', ice_cream.get('메로나'))        # 메로나 가격 :  1000
print('메로나 가격 : ', ice_cream['메로나'])            # 메로나 가격 :  1000

# 5
ice_cream.update(메로나=1300)
print(ice_cream)                # {'메로나': 1300, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500} 

ice_cream2['메로나'] = 1300
print(ice_cream2)               # {'메로나': 1300, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}

# 6
del ice_cream['메로나']
print(ice_cream)                # {'폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}

# 7
ice_cream = dict(
    메로나=[300, 20],
    비비빅=[400,3],
    죠스바=[250,100]
)
print(ice_cream)                # {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}

# 8
print('{0}원'.format(ice_cream['메로나'][0]))   # 300원

# 9
print(ice_cream.keys())         # dict_keys(['메로나', '비비빅', '죠스바'])

# 10
print(ice_cream.values())       # dict_values([[300, 20], [400, 3], [250, 100]])

# 11
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice_sum = list(icecream.values())
print(sum(ice_sum))

print(sum(icecream.values()))

# 12
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)                   # {'apple': 300, 'pear': 250, 'peach': 400}

# 13
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)              # {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}