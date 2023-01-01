# list 형식으로 문자열 입력
music = list(map(int, input().split()))

# 오름차순 정렬 시 
if music == sorted(music):
    print('ascending')

# 내림차순 정렬 시
elif music == sorted(music, reverse=True):
    print('descending')

# 순서 없을 시
else:
    print('mixed')