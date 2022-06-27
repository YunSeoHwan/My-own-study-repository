# Chapter09_1
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, 텍스트 모드 : t, 바이너리 모드 : b
# 상대 경로 ('../, ./'), 절대 경로('C:\asdf\example...')

# 파일 읽기
# 예제1

f = open('./Basic/chapter09/resource/it_news.txt', 'r', encoding='UTF-8')

# 속성 확인
print(dir(f))
# 인코딩 확인                    # UTF-8
print(f.encoding)
# 파일 이름
print(f.name)                   # ./Basic/chapter09/resource/it_news.txt
# 모드 확인
print(f.mode)                   # r

cts = f.read()
print(cts)

# 반드시 close
f.close()