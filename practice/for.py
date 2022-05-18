# 1
meau = ['김밥', '라면', '튀김']
for m in meau:
    print('오늘의 메뉴 : ', m)

# 2
stock = ['SK하이닉스', '카카오', '삼성전자']
for s in stock:
    print(len(s))                       # 6 3 4

# 3
lang = ['a', 'b', 'c', 'd']
for l in lang[1:]:
    print(l)                            # b c d
print()

# 4 
for l in lang[::2]:
    print(l)                            # a c
print()

# 5
for l in lang[::-1]:
    print(l)                            # d c b a
print()