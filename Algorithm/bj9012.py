import sys
m = int(sys.stdin.readline())

for i in range(m):
    right = 0
    left = 0
    a = input()
    # 한글자씩 분리해서 list화
    b = list(a)
    for j in range(len(b)):
        # 괄호 counting
        if b[j] == '(':
            left += 1
        elif b[j] ==')':
            right += 1
        
        # ) 괄호의 수가 ( 수보다 크면 종료
        if right > left:
            print('NO')
            break
    # break 탈출 후, 중복 처리 방지    
    if right <= left:
        if right == left:
            print("YES")
        elif right != left:
            print('NO')