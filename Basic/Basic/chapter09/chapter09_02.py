# Chapter09_02
# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv

import csv

# 예제1
with open('./Basic/chapter09/resource/test1.csv', 'r') as f:
    reader = csv.reader(f)

    next(reader)            # header skip
    # 객체 확인
    print(reader)

    # 타입 확인
    print(type(reader))

    # 속성 확인
    print(dir(reader))      # __iter__ 

    for c in reader:
        print(c)            # list로 가져옴
        # list to str
        print(' : '.join(c))

# 예제2
with open('./Basic/chapter09/resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')       # 구분 기호

    for c in reader:
        print(c)

# 예제3
with open('./Basic/chapter09/resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)

    print(reader)

    for c in reader:
        for k,v in c.items():
            print(k, v)
        print('--------------------')

# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./Basic/chapter09/resource/write1.csv', 'w', encoding='utf-8', newline='') as f:
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    # print(dir(wt))
    # 타입 확인
    # print(type(wt))
    
    for v in w:
        wt.writerow(v)          # 한 줄씩 쓰기

# 예제5
with open('./Basic/chapter09/resource/write2.csv', 'w', encoding='utf-8', newline='') as f:
    # 필드명
    fields = ['One', 'Two','Three']

    # DictWriter
    wt = csv.DictWriter(f, fieldnames=fields)

    # Header Write
    wt.writeheader()

    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})