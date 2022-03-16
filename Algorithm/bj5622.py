dial = input()
change_list = []
ascii_list = []
sum = 0
change_list = list(dial)

for i in change_list:
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