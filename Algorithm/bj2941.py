alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']   # 해당 값 리스트

word = input()  # 사용자 값

for i in alpha:     # 리스트 값 불러옴
    if i in word:   # 사용자 값에 리스트 값이 있으면 다른문자로 대체
        word = word.replace(i,'*')

print(len(word))