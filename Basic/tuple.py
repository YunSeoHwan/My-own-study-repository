# 1
movie_rank = ()
print(movie_rank)                       # ()

# 2
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)                       # ('닥터 스트레인지', '스플릿', '럭키')

# 3
a = (1,)
print(a)                                # (1, )

# 4
t = 1, 2, 3, 4
print(type(t))                          # <class 'tuple'>

# 5
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')

print(t)                                # ('A', 'b', 'c')

# 6
interest = ('삼성전자', '카카오', 'Naver')
new_interest = list(interest)
print(new_interest)                     # ['삼성전자', '카카오', 'Naver']

# 7
a = tuple(range(2, 100, 2))
print(a)