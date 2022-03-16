dial = input()
change_list = []    # string을 list로 변환 리스트
ascii_list = []     # list값 ascii로 변환 리스트
sum = 0
change_list = list(dial)

for i in change_list:       # ascii로 변환
  ascii_list.append(ord(i))

for i in range(len(ascii_list)):
    if ascii_list[i] >= 65 and ascii_list[i] <= 67:
        ascii_list[i] = 3
    elif ascii_list[i] >= 68 and ascii_list[i] <= 70:
        ascii_list[i] = 4
    elif ascii_list[i] >= 71 and ascii_list[i] <= 73:
        ascii_list[i] = 5        
    elif ascii_list[i] >= 74 and ascii_list[i] <= 76:
        ascii_list[i] = 6
    elif ascii_list[i] >= 77 and ascii_list[i] <= 79:
        ascii_list[i] = 7
    elif ascii_list[i] >= 80 and ascii_list[i] <= 83:
        ascii_list[i] = 8
    elif ascii_list[i] >= 84 and ascii_list[i] <= 86:
        ascii_list[i] = 9
    elif ascii_list[i] >= 87 and ascii_list[i] <= 90:
        ascii_list[i] = 10

for i in range(len(ascii_list)):
  sum += ascii_list[i]

print(sum)


# 좋은 풀이법
alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alpabet_list :  
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in word :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                time += alpabet_list.index(unit) +3  # time = time + index + 3
print(time)
