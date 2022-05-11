# 1
from audioop import avg


movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)               # ['닥터 스트레인지', '스플릿', '럭키']

# 2
movie_rank.append('배트맨')
print(movie_rank)               # ['닥터 스트레인지', '스플릿', '럭키', '배트맨']

# 3
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)               # ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

# 4
movie_rank.remove('럭키')       # del movie_rank[2]
print(movie_rank)               # ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

# 5
lang1 = ['C', 'C++', 'JAVA']
lang2 = ['Python', 'Go', 'C#']
langs = lang1 + lang2
print(langs)                    # ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']

# 6
nums = [1, 2, 3, 4, 5]
print(sum(nums))                # 15

# 7
print(len(nums))                # 5

# 8
print(sum(nums) / len(nums))    # 3.0

# 9
price = ['20220511', 100, 130, 140, 150, 160, 170]
print(price[1:])                # [100, 130, 140, 150, 160, 170]

# 10
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])               # [1, 3, 5, 7, 9]
print(nums[1::2])              # [2, 4, 6, 8, 10]

# 11
print(nums[::-1])              # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 12
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])     # 삼성전자 Naver

# 13
interest = ['삼성전자', 'LG전자', 'Naver', '카카오', '쿠팡']
new_interest = "/".join(interest)
print(new_interest)                 # 삼성전자/LG전자/Naver/카카오/쿠팡

# 14
a1 = [6, 3, 9]
print('a1:', a1)
a2 = a1.sort() 
print('-----정렬 후-----')
print('a1:', a1)
print('a2:', a2)

# 15
b1 = [6, 3, 9]
print('b1:', b1)
b2 = sorted(b1) 
print('-----정렬 후-----')
print('b1:', b1)
print('b2:', b2)

# a1: [6, 3, 9]
# -----정렬 후-----
# a1: [3, 6, 9]
# a2: None
# b1: [6, 3, 9]
# -----정렬 후-----
# b1: [6, 3, 9]
# b2: [3, 6, 9]