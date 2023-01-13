import sys

input = sys.stdin.readline

n = int(input())

# stack, 배열, 연산
stack = []
arr = []
op = []
for _ in range(n):
    arr.append(int(input()))

# 1씩 증가해주는 변수
cnt = 1
while True:

    # 해당 배열이 0이면 정답처리
    if len(arr) == 0:
        break

    # stack이 0 이면 값 추가
    if len(stack) == 0:
        stack.append(cnt)
        cnt += 1
        op.append('+')
    
    # stack 0이 아니면 비교
    else:
        # stack값이 더 크면 종료
        if arr[0] < stack[-1]:
            print('NO')
            sys.exit()

        # 동일하면 각각 제거
        elif arr[0] == stack[-1]:
            arr.remove(arr[0])
            stack.pop()
            op.append('-')
        
        # 그렇지 않으면 값추가
        else:
            stack.append(cnt)
            cnt+=1
            op.append('+')

for i in op:
    print(i)