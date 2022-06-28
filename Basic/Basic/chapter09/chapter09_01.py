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

# 예제2
with open('./Basic/chapter09/resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
    # close 자동 실행

# 예제3
# read() : 전체 읽기, read(10) : 10Byte

with open('./Basic/chapter09/resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)                        # Right now gamers can
    c = f.read(20)
    print(c)                        #  pay just $1 for acc  -> 커서가 뒤로 이동
    f.seek(0,0)                     # 첫 줄로 커서 이동
    c = f.read(20)
    print(c)                        # Right now gamers can

# 예제4
# readline : 한 줄 씩 읽기

with open('./Basic/chapter09/resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()             # 한 줄 출력
    print(line)                     # Right now gamers can pay just $1 for access to hundreds of titles across PC

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장

with open('./Basic/chapter09/resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts  = f.readlines()
    print(cts)
    for c in cts:
        print(c, end='')            # 한 줄씩 전체 출력

# 파일 쓰기(write)

# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python2\n')
    
    
# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)
    
# 예제4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)