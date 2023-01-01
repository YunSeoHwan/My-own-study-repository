while True:
    # 반복 횟수 지정
    num = input()

    # 0 입력시 break
    if num == str(0):
        break
    # 앞뒤 문자열 슬라이싱
    if num[0:] == num[::-1]:
        print('yes')
    else:
        print('no')